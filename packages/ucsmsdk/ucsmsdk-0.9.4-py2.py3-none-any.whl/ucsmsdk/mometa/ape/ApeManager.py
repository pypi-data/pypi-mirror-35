"""This module contains the general information for ApeManager ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ApeManagerConsts:
    pass


class ApeManager(ManagedObject):
    """This is ApeManager class."""

    consts = ApeManagerConsts()
    naming_props = set([])

    mo_meta = MoMeta("ApeManager", "apeManager", "ape", VersionMeta.Version101e, "InputOutput", 0x1f, [], ["read-only"], [u'topRoot'], [u'apeControllerManager', u'apeDcosAgManager', u'apeHostAgent', u'apeLANBoot', u'apeLocalDiskBoot', u'apeMc', u'apeNicAgManager', u'apeSANBoot', u'apeVirtualMediaBoot'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "stats_update_id": MoPropertyMeta("stats_update_id", "statsUpdateId", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "statsUpdateId": "stats_update_id", 
        "status": "status", 
    }

    def __init__(self, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.sacl = None
        self.stats_update_id = None
        self.status = None

        ManagedObject.__init__(self, "ApeManager", **kwargs)
