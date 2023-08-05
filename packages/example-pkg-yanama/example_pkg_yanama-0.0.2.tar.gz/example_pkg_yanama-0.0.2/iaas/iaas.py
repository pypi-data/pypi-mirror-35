import yaml

from chpapi import CHPAPIClass
from xstream import XstreamClass

class IAASAbstractClass():
    load = None
    chpapi_instance = None
    xstream_instance = None
    dict_factory_method = {}
    def __init__(self, abstract_file_path=None):
        try:
            self.chpapi_instance = CHPAPIClass() 
            self.xstream_instance = XstreamClass()
            p_file = open(abstract_file_path, "r+")
            loaded_data = yaml.load(p_file)
            p_file.close()
            print(loaded_data['Xstream'])
            if 'Xstream' in loaded_data and loaded_data['Xstream'] is not None and len(loaded_data['Xstream']) > 0:
                for a_method in loaded_data['Xstream']:
                    self.dict_factory_method[a_method] = self.xstream_instance
            if 'Chpapi' in loaded_data and loaded_data['Chpapi'] is not None and len(loaded_data['Chpapi']) > 0:
                for a_method in loaded_data['Chpapi']:
                    self.dict_factory_method[a_method] = self.chpapi_instance
        except Exception as ex:
            template = "Exception: An exception of type {0} occured: {1}"
            message = template.format(type(ex).__name__, str(ex))
            raise Exception(message)
 
    def create_tenant(self):
        try:
            self.dict_factory_method['create_tenant'].create_tenant()
        except Exception as ex:
            template = "Exception: An exception of type {0} occured: {1}"
            message = template.format(type(ex).__name__, str(ex))
            raise Exception(message)
        return 

    def create_user(self):
        try:
            self.dict_factory_method['create_user'].create_user()
        except Exception as ex:
            template = "Exception: An exception of type {0} occured: {1}"
            message = template.format(type(ex).__name__, str(ex))
            raise Exception(message)
        return 

    def create_vm(self, vm_details):
        result = False
        try:
            result = self.dict_factory_method['create_vm'].create_vm(vm_details)
        except Exception as ex:
            template = "Exception: An exception of type {0} occured: {1}"
            message = template.format(type(ex).__name__, str(ex))
            raise Exception(message)
        return result

    def create_storage(self):
        try:
            self.dict_factory_method['create_storage'].create_storage()
        except Exception as ex:
            template = "Exception: An exception of type {0} occured: {1}"
            message = template.format(type(ex).__name__, str(ex))
            raise Exception(message)
        return 

    def create_network(self):
        try:
            self.dict_factory_method['create_network'].create_network()
        except Exception as ex:
            template = "Exception: An exception of type {0} occured: {1}"
            message = template.format(type(ex).__name__, str(ex))
            raise Exception(message)
        return 

    def create_compute(self):
        try:
            self.dict_factory_method['create_vm'].create_vm()
        except Exception as ex:
            template = "Exception: An exception of type {0} occured: {1}"
            message = template.format(type(ex).__name__, str(ex))
            raise Exception(message)
        return 

    def assign_network_to_tenant(self):
        try:
            self.dict_factory_method['create_vm'].create_vm()
        except Exception as ex:
            template = "Exception: An exception of type {0} occured: {1}"
            message = template.format(type(ex).__name__, str(ex))
            raise Exception(message)
        return 

    def assign_storage_to_tenant(self):
        try:
            self.dict_factory_method['create_vm'].create_vm()
        except Exception as ex:
            template = "Exception: An exception of type {0} occured: {1}"
            message = template.format(type(ex).__name__, str(ex))
            raise Exception(message)
        return 

    def assign_compute_to_tenant(self):
        try:
            self.dict_factory_method['create_vm'].create_vm()
        except Exception as ex:
            template = "Exception: An exception of type {0} occured: {1}"
            message = template.format(type(ex).__name__, str(ex))
            raise Exception(message)
        return 

    def populate_network_for_all(self):
        try:
            self.dict_factory_method['create_vm'].create_vm()
        except Exception as ex:
            template = "Exception: An exception of type {0} occured: {1}"
            message = template.format(type(ex).__name__, str(ex))
            raise Exception(message)
        return 

#v = {'HardwareTemplateID': 'a66e0d2a-587e-4bd0-9802-853b2c75185d', 'Disks': [{'UnitNumber': 0, 'CapacityKB': 16777216, 'FreeSpaceKB': 'null', 'DiskMode': 5, 'VirtualMachineDiskID': 'e26a72cf-e3fb-f052-2659-b865b45244ba', 'freeSpaceUnit': '', 'scsiLabel': 'SCSI 0', 'ControllerBusNumber': 0, 'StorageProfileID': '40aee1c1-13a9-46ea-81c7-ca91e7f96247', 'DiskFileName': '[part-c04-s01-localDS] A001US014XVM454/A001US014XVM454-000003.vmdk', 'StorageID': 'null', 'computeAllocationID': '0341ac9e-9ff3-7443-3fa9-597a71998cdf', 'freeSpace': 0, 'capacityUnit': '', 'DiskNumber': 1, 'DeviceKey': 2000, 'StorageIdentifier': 'datastore-12', 'StorageProfileName': 'LAB - Tier II Block Storage - LOCAL', 'capacity': 0}], 'CustomerDefinedName': 'Sheetal_vm_1', 'SourceTemplateID': '31459e49-7d33-1627-d63e-7130e87b529f', 'ComputeProfileID': '4f44c852-1a0b-4343-8f22-6ba6d52e1263', 'Hypervisor': {'Site': {'SiteID': '69d29e4b-ce66-66b9-a07d-c4612616bb0f'}}}

#test = IAASAbstractClass("api_config.yaml")
#test.populate_network_for_all()
