"""This module contains the general information for OsInstance ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class OsInstanceConsts:
    TYPE_LINUX = "Linux"
    TYPE_PNU_OS = "PnuOS"
    TYPE_SOLARIS = "Solaris"
    TYPE_VMWARE_ESX = "VMWareESX"
    TYPE_WINDOWS = "Windows"
    TYPE_UNSPECIFIED = "unspecified"


class OsInstance(ManagedObject):
    """This is OsInstance class."""

    consts = OsInstanceConsts()
    naming_props = set([])

    mo_meta = MoMeta("OsInstance", "osInstance", "os", VersionMeta.Version101e, "InputOutput", 0x1f, [], ["read-only"], [u'computeBlade', u'computeRackUnit', u'computeServerUnit'], [u'osEthBondIntf', u'osEthIntf'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "kernel_name": MoPropertyMeta("kernel_name", "kernelName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "kernel_release": MoPropertyMeta("kernel_release", "kernelRelease", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "kernel_version": MoPropertyMeta("kernel_version", "kernelVersion", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Linux", "PnuOS", "Solaris", "VMWareESX", "Windows", "unspecified"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "hostname": "hostname", 
        "kernelName": "kernel_name", 
        "kernelRelease": "kernel_release", 
        "kernelVersion": "kernel_version", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.hostname = None
        self.kernel_name = None
        self.kernel_release = None
        self.kernel_version = None
        self.name = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "OsInstance", parent_mo_or_dn, **kwargs)
