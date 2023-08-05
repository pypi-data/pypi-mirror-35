# Make sure to have unique matches in different lines
# Order the list in alphabetical order based on the "issue" key
whitelist = [
    {"issue": "https://jira.opendaylight.org/browse/NETVIRT-972",
     "id": "ConflictingModificationAppliedException",
     "context": [
         "Node was created by other transaction",
         "Optimistic lock failed for path /(urn:opendaylight:inventory?revision=2013-08-19)nodes/node/node" +
         "[{(urn:opendaylight:inventory?revision=2013-08-19)id=openflow",
         "table/table[{(urn:opendaylight:flow:inventory?revision=2013-08-19)id=21}]/flow/flow" +
         "[{(urn:opendaylight:flow:inventory?revision=2013-08-19)id=L3."
     ]},
    # oxygen
    {"issue": "https://jira.opendaylight.org/browse/NETVIRT-972",
     "id": "ConflictingModificationAppliedException",
     "context": [
         "Node was created by other transaction",
         "OptimisticLockFailedException: Optimistic lock failed."
         "Conflicting modification for path /(urn:opendaylight:inventory?revision=2013-08-19)nodes/node/node" +
         "[{(urn:opendaylight:inventory?revision=2013-08-19)id=",
         "table/table[{(urn:opendaylight:flow:inventory?revision=2013-08-19)id=21}]/flow/flow" +
         "[{(urn:opendaylight:flow:inventory?revision=2013-08-19)id=L3.", ".21.", ".42."
     ]},
    {"issue": "https://jira.opendaylight.org/browse/NETVIRT-1135",
     "id": "ConflictingModificationAppliedException",
     "context": [
         "Node was created by other transaction",
         "Optimistic lock failed for path /(urn:opendaylight:inventory?revision=2013-08-19)nodes/node/node" +
         "[{(urn:opendaylight:inventory?revision=2013-08-19)id=openflow:",
     ]},
    # oxygen
    {"issue": "https://jira.opendaylight.org/browse/NETVIRT-1135",
     "id": "ConflictingModificationAppliedException",
     "context": [
         "OptimisticLockFailedException: Optimistic lock failed."
         "Conflicting modification for path /(urn:opendaylight:inventory?revision=2013-08-19)nodes/node/node" +
         "[{(urn:opendaylight:inventory?revision=2013-08-19)id=openflow:",
         "table/table[{(urn:opendaylight:flow:inventory?revision=2013-08-19)id=47}]/flow/flow" +
         "[{(urn:opendaylight:flow:inventory?revision=2013-08-19)id=SNAT.", ".47."
     ]},
    {"issue": "https://jira.opendaylight.org/browse/NETVIRT-1136",
     "id": "ConflictingModificationAppliedException",
     "context": [
         "Node was deleted by other transaction",
         "Optimistic lock failed for path /(urn:opendaylight:netvirt:elan?revision=2015-06-02)elan-" +
         "forwarding-tables/mac-table/mac-table[{(urn:opendaylight:netvirt:elan?revision=2015-06-02)" +
         "elan-instance-name=",
     ]},
    # oxygen version of NETVIRT-1136
    {"issue": "https://jira.opendaylight.org/browse/NETVIRT-1136",
     "id": "ConflictingModificationAppliedException",
     "context": [
         "Node was deleted by other transaction",
         "OptimisticLockFailedException: Optimistic lock failed.",
         "Conflicting modification for path /(urn:opendaylight:netvirt:elan?revision=2015-06-02)elan-" +
         "forwarding-tables/mac-table/mac-table[{(urn:opendaylight:netvirt:elan?revision=2015-06-02)" +
         "elan-instance-name="
     ]},
    {"issue": "https://jira.opendaylight.org/browse/NETVIRT-1260",
     "id": "ConflictingModificationAppliedException",
     "context": [
         "Optimistic lock failed for path /(urn:ietf:params:xml:ns:yang:ietf-interfaces?revision=2014-05-08)" +
         "interfaces/interface/interface[{(urn:ietf:params:xml:ns:yang:ietf-interfaces?revision=2014-05-08)name=",
     ]},
    {"issue": "https://jira.opendaylight.org/browse/NETVIRT-1270",
     "id": "ConflictingModificationAppliedException",
     "context": [
         "OptimisticLockFailedException",
         "/(urn:opendaylight:netvirt:l3vpn?revision=2013-09-11)" +
         "vpn-instance-op-data/vpn-instance-op-data-entry/vpn-instance-op-data-entry" +
         "[{(urn:opendaylight:netvirt:l3vpn?revision=2013-09-11)vrf-id=",
         "vrf-id=", "/vpn-to-dpn-list/vpn-to-dpn-list", "dpnId="
     ]},
    {"issue": "https://jira.opendaylight.org/browse/NETVIRT-1270",
     "id": "ExecutionException",
     "context": [
         "OptimisticLockFailedException: Optimistic lock failed",
         "removeOrUpdateVpnToDpnList: Error removing from dpnToVpnList for vpn "
     ]},
    {"issue": "https://jira.opendaylight.org/browse/NETVIRT-1270",
     "id": "OptimisticLockFailedException",
     "context": [
         "OptimisticLockFailedException",
         "VpnInterfaceOpListener",
         "Direct Exception (not failed Future) when executing job, won't even retry: JobEntry{key='VPNINTERFACE-",
         "vpn-instance-op-data/vpn-instance-op-data-entry/vpn-instance-op-data-entry" +
         "[{(urn:opendaylight:netvirt:l3vpn?revision=2013-09-11)vrf-id=",
         "vrf-id=", "/vpn-to-dpn-list/vpn-to-dpn-list", "dpnId="
     ]},
    {"issue": "https://jira.opendaylight.org/browse/NETVIRT-1281",
     "id": "OptimisticLockFailedException",
     "context": [
         "OptimisticLockFailedException: Optimistic lock failed.",
         "ConflictingModificationAppliedException: Node children was modified by other transaction",
         "Direct Exception (not failed Future) when executing job, won't even retry: JobEntry{key='VPNINTERFACE-"
     ]},
    {"issue": "https://jira.opendaylight.org/browse/NETVIRT-1304",
     "id": "ModifiedNodeDoesNotExistException",
     "context": [
         "ModifiedNodeDoesNotExistException",
         "/(urn:opendaylight:netvirt:fibmanager?revision=2015-03-30)fibEntries/" +
         "vrfTables/vrfTables[{(urn:opendaylight:netvirt:fibmanager?revision=2015-03-30)routeDistinguisher="
     ]},
    {"issue": "https://jira.opendaylight.org/browse/NETVIRT-1304",
     "id": "TransactionCommitFailedException",
     "context": [
         "TransactionCommitFailedException",
         "/(urn:opendaylight:netvirt:fibmanager?revision=2015-03-30)fibEntries/" +
         "vrfTables/vrfTables[{(urn:opendaylight:netvirt:fibmanager?revision=2015-03-30)routeDistinguisher="
     ]},
    {"issue": "https://jira.opendaylight.org/browse/NEUTRON-157",
     "id": "ConflictingModificationAppliedException",
     "context": [
         "Optimistic lock failed for path /(urn:opendaylight:neutron?revision=2015-07-12)" +
         "neutron/networks/network/network[{(urn:opendaylight:neutron?revision=2015-07-12)uuid=",
         "Conflicting modification for path /(urn:opendaylight:neutron?revision=2015-07-12)" +
         "neutron/networks/network/network[{(urn:opendaylight:neutron?revision=2015-07-12)uuid="
     ]},
    {"issue": "https://jira.opendaylight.org/browse/NEUTRON-157",
     "id": "OptimisticLockFailedException",
     "context": [
         "Got OptimisticLockFailedException",
         "AbstractTranscriberInterface"
     ]},
    {"issue": "https://jira.opendaylight.org/browse/NEUTRON-157",
     "id": "ConflictingModificationAppliedException",
     "context": [
         "Optimistic lock failed for path /(urn:opendaylight:neutron?revision=2015-07-12)neutron"
     ]},
    # oxygen
    {"issue": "https://jira.opendaylight.org/browse/NEUTRON-157",
     "id": "ConflictingModificationAppliedException",
     "context": [
         "OptimisticLockFailedException: Optimistic lock failed.",
         "Conflicting modification for path /(urn:opendaylight:neutron?revision=2015-07-12)" +
         "neutron/networks/network/network[{(urn:opendaylight:neutron?revision=2015-07-12)uuid=",
     ]},
    {"issue": "https://jira.opendaylight.org/browse/OPNFLWPLUG-917",
     "id": "IllegalStateException",
     "context": [
         "java.lang.IllegalStateException: Deserializer for key: msgVersion: 4 objectClass: " +
         "org.opendaylight.yang.gen.v1.urn.opendaylight.openflow.oxm.rev150225.match.entries.grouping.MatchEntry " +
         "msgType: 1 oxm_field: 33 experimenterID: null was not found " +
         "- please verify that all needed deserializers ale loaded correctly"
     ]}
]
