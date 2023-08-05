import collections
import errno
import json
import logging
import os
import re

from odltools.common import files

logger = logging.getLogger("karaf.excepts")
OUTFILE = "/tmp/karaf.exceptions.txt"
LOGFILE = "/tmp/karaf.log"
WLFILE = "/tmp/whitelist.exceptions.json"

_re_ts = re.compile(r"^[0-9]{4}(-[0-9]{2}){2}T([0-9]{2}:){2}[0-9]{2},[0-9]{3}")
_re_ts_we = re.compile(r"^[0-9]{4}(-[0-9]{2}){2}T([0-9]{2}:){2}[0-9]{2},[0-9]{3}( \| ERROR \| | \| WARN {2}\| )")
_re_ex = re.compile(r"(?i)exception")
_ex_map = collections.OrderedDict()
_ts_list = []
_fail = []
_ftell = None
whitelist = {}


def get_exceptions(lines):
    """
    Create a map of exceptions that also has a list of warnings and errors preceding
    the exception to use as context.

    The lines are parsed to create a list where all lines related to a timestamp
    are aggregated. Timestamped lines with exception (case insensitive) are copied
    to the exception map keyed to the index of the timestamp line. Each exception value
    also has a list containing WARN and ERROR lines proceeding the exception.

    :param list lines:
    :return OrderedDict _ex_map: map of exceptions
    """
    global _ex_map
    _ex_map = collections.OrderedDict()
    global _ts_list
    _ts_list = []
    cur_list = []
    warnerr_deq = collections.deque(maxlen=5)

    for line in lines:
        ts = _re_ts.search(line)

        # Check if this is the start or continuation of a timestamp line
        if ts:
            cur_list = [line]
            _ts_list.append(cur_list)
            ts_we = _re_ts_we.search(line)
            # Track WARN and ERROR lines
            if ts_we:
                warn_err_index = len(_ts_list) - 1
                warnerr_deq.append(warn_err_index)
        # Append to current timestamp line since this is not a timestamp line
        else:
            cur_list.append(line)

        # Add the timestamp line to the exception map if it has an exception
        ex = _re_ex.search(line)
        if ex:
            index = len(_ts_list) - 1
            if index not in _ex_map:
                _ex_map[index] = {"warnerr_list": list(warnerr_deq), 'lines': cur_list}
                warnerr_deq.clear()  # reset the deque to only track new ERROR and WARN lines

    return _ex_map


def check_exceptions(whitelist):
    """
    Return a list of exceptions that were not in the whitelist.

    Each exception found is compared against all the patterns
    in the whitelist.

    :param list whitelist: list of whitelist exceptions
    :return list _fail: list of exceptions not in the whitelist
    """
    global _fail
    _fail = []
    _match = []

    for ex_idx, ex in _ex_map.items():
        ex_str = "__".join(ex.get("lines"))
        for wl_ex in whitelist:
            # skip the current whitelist exception if not in the current exception
            if wl_ex.get("id") not in ex_str:
                continue
            wl_contexts = wl_ex.get("context")
            num_context_matches = 0
            for wl_context in wl_contexts:
                for exwe_index in reversed(ex.get("warnerr_list")):
                    exwe_str = "__".join(_ts_list[exwe_index])
                    if wl_context in exwe_str:
                        num_context_matches += 1
            # Mark this exception as a known issue if all the context's matched
            if num_context_matches >= len(wl_contexts):
                ex["issue"] = wl_ex.get("issue")
                _match.append(ex)
                logger.debug("known exception was seen: {}".format(ex["issue"]))
                break
        # A new exception when it isn't marked with a known issue.
        if "issue" not in ex:
            _fail.append(ex)
    return _fail, _match


def verify_exceptions(lines, whitelist):
    """
    Return a list of exceptions not in the whitelist for the given lines.

    :param list lines: list of lines from a log
    :param list whitelist: list of whitelist exceptions
    :return list, list: one list of exceptions not in the whitelist, and a second with matching issues
    """
    if not lines:
        return
    get_exceptions(lines)
    return check_exceptions(whitelist)


def write_exceptions_map_to_file(testname, filename, mode="a+"):
    """
    Write the exceptions map to a file under the testname header. The output
    will include all lines in the exception itself as well as any previous
    contextual warning or error lines. The output will be appended or overwritten
    depending on the mode parameter. It is assumed that the caller has called
    verify_exceptions() earlier to populate the exceptions map, otherwise only
    the testname and header will be printed to the file.

    :param str testname: The name of the test
    :param str filename: The file to open for writing
    :param str mode: Append (a+) or overwrite (w+)
    """
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    with open(filename, mode) as fp:
        fp.write("{}\n".format("=" * 60))
        fp.write("Starting test: {}\n".format(testname))
        for ex_idx, ex in _ex_map.items():
            fp.write("{}\n".format("-" * 40))
            if "issue" in ex:
                fp.write("Exception was matched to: {}\n".format(ex.get("issue")))
            else:
                fp.write("Exception is new\n")
            for exwe_index in ex.get("warnerr_list")[:-1]:
                for line in _ts_list[exwe_index]:
                    fp.write("{}\n".format(line))
            fp.writelines(ex.get("lines"))
            fp.write("\n")


def read_file(fname):
    with open(fname) as f:
        lines = f.readlines()
    return lines


def get_test_lines_from_log(fname, testname=None, search=None):
    # ROBOT MESSAGE: Starting test 01 l2.Create Vm Instances For net_2
    starttest = "ROBOT MESSAGE: Starting test "
    starttestname = None
    if testname is not None:
        starttestname = "{} {}".format(starttest, testname)
    testlines = []
    # re_starttest = re.compile(r'(' + starttest + ')' + stack_re + ')')
    with open(fname) as fp:
        for line in fp:
            if len(testlines) == 0:
                if testname:
                    if starttestname not in line:
                        # Keep reading until the line with the starting testname is found
                        continue
                elif True:
                    pass
                else:
                    testlines.append(line)
            else:
                if starttest in line:
                    # The next test is starting so stop processing lines
                    break
                if search is not None:
                    if search in line:
                        testlines.append(line)
                else:
                    testlines.append(line)
    return testlines


def print_exceptions():
    for ex in _fail:
        for line in ex.get("lines"):
            print("{}".format(line))


def get_and_verify_exceptions(logfile, outfile, wlfile, tname=None, mode="a+", noprint=False):
    # ROBOT MESSAGE: Starting test 01 l2.Ping Vm Instance1 In net_1
    res_starting_suite = "^.* ROBOT MESSAGE: Starting suite (.*)$"
    res_starting_test = "^.* ROBOT MESSAGE: Starting test (.*)$"
    if tname:
        res_starting_test = "^.* ROBOT MESSAGE: Starting test (.*)$"
    res_start = "|".join("(?:{0})".format(x) for x in (res_starting_suite, res_starting_test))
    re_start = re.compile(res_start)

    logger.info("run: processing {} for exceptions, output written to: {}".format(logfile, outfile))

    if os.path.isfile(wlfile) is False:
        print("Whitelist exception file {} does not exist.".format(wlfile))
        return
    whitelist = get_whitelist(wlfile)

    if os.path.isfile(logfile) is False:
        print("Karaf logfile {} does not exist.".format(logfile))
        return

    if mode == "w":
        files.writelines(outfile, [])

    testlines = []
    current_testname = "No test"
    with open(logfile, 'r') as fp:
        for line in fp:
            match = re_start.search(line)
            if match:
                testname = match.group(1) or match.group(2)
                if tname:
                    if tname == current_testname:
                        verify_exceptions(testlines, whitelist)
                        write_exceptions_map_to_file(current_testname, outfile)
                        if not noprint:
                            print_exceptions()
                        testlines = []
                        current_testname = "No test"
                        break
                    elif tname != testname:
                        continue
                logger.debug("run: found new test: {}".format(testname))
                if testlines:
                    verify_exceptions(testlines, whitelist)
                    write_exceptions_map_to_file(current_testname, outfile)
                    if not noprint:
                        print_exceptions()
                    testlines = [line]
                    current_testname = testname
                else:
                    testlines = [line]
                    current_testname = testname
            elif testlines:
                testlines.append(line)
        _ftell = fp.tell()
    if testlines:
        verify_exceptions(testlines, whitelist)
        write_exceptions_map_to_file(current_testname, outfile)
        if not noprint:
            print_exceptions()


def get_whitelist(wlfile):
    global whitelist
    wljson = files.read(wlfile)
    whitelist = json.loads(wljson).get("whitelist")
    return whitelist


def run(args):
    outfile = args.outfile or OUTFILE
    logfile = args.logfile or LOGFILE
    wlfile = args.wlfile or WLFILE
    tname = args.testname or None
    noprint = args.noprint or False
    mode = "w"

    get_and_verify_exceptions(logfile, outfile, wlfile, tname, mode, noprint)
