"""This module contains the general information for StorageSasLinkDescriptor ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StorageSasLinkDescriptorConsts:
    CONTROLLER_TYPE_FLASH = "FLASH"
    CONTROLLER_TYPE_HBA = "HBA"
    CONTROLLER_TYPE_M2 = "M2"
    CONTROLLER_TYPE_NVME = "NVME"
    CONTROLLER_TYPE_PCH = "PCH"
    CONTROLLER_TYPE_PT = "PT"
    CONTROLLER_TYPE_SAS = "SAS"
    CONTROLLER_TYPE_SATA = "SATA"
    CONTROLLER_TYPE_SD = "SD"
    CONTROLLER_TYPE_EXTERNAL = "external"
    CONTROLLER_TYPE_UNKNOWN = "unknown"


class StorageSasLinkDescriptor(ManagedObject):
    """This is StorageSasLinkDescriptor class."""

    consts = StorageSasLinkDescriptorConsts()
    naming_props = set([u'serverId', u'controllerType', u'controllerId', u'id'])

    mo_meta = MoMeta("StorageSasLinkDescriptor", "storageSasLinkDescriptor", "sas-link-desc-server-[server_id]-controller-[controller_type]-[controller_id]-id-[id]", VersionMeta.Version312b, "InputOutput", 0x1ff, [], [""], [u'equipmentChassisCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "controller_id": MoPropertyMeta("controller_id", "controllerId", "uint", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "controller_type": MoPropertyMeta("controller_type", "controllerType", "string", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x8, None, None, None, ["FLASH", "HBA", "M2", "NVME", "PCH", "PT", "SAS", "SATA", "SD", "external", "unknown"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []), 
        "link_descr": MoPropertyMeta("link_descr", "linkDescr", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "server_id": MoPropertyMeta("server_id", "serverId", "uint", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x80, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "controllerId": "controller_id", 
        "controllerType": "controller_type", 
        "dn": "dn", 
        "id": "id", 
        "linkDescr": "link_descr", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serverId": "server_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, server_id, controller_type, controller_id, id, **kwargs):
        self._dirty_mask = 0
        self.server_id = server_id
        self.controller_type = controller_type
        self.controller_id = controller_id
        self.id = id
        self.child_action = None
        self.link_descr = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "StorageSasLinkDescriptor", parent_mo_or_dn, **kwargs)
