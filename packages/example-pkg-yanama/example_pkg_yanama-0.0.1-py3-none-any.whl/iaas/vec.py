"""
Manages the xStream API calls and retrieve the contents
"""

import requests

from time import sleep

from common.functions import get_config
from common.constants import KEY_XSTREAM, WAIT_TIME_BETWEEN_REQUESTS


class Xstream:
    """
    Class to connect with github and perform various operations on github
    """

    def __init__(self, login=None, password=None, host=None, api_version=None):
        if not login:
            self.login = get_config(KEY_XSTREAM, "username")
        else:
            self.login = login

        if not password:
            self.password = get_config(KEY_XSTREAM, "password")
        else:
            self.password = password

        if not host:
            self.host = get_config(KEY_XSTREAM, "host")
        else:
            self.host = host

        if not api_version:
            self.api_version = get_config(KEY_XSTREAM, "api_version")
        else:
            self.api_version = api_version

        self.request_header = {'Accept': "application/json", 'Content-Type': "application/json"}
        self.XTM_TOKEN = None
        self.tenant_id = None

    def url(self, api_name):
        return "https://%s/api/%s/%s/" % (self.host, self.api_version, api_name)

    def authenticate(self):
        """
        Authenticate against github
        :return: status code
        """

        response = requests.post(self.url("auth"), headers=self.request_header,
                                 json={"username": self.login, "password": self.password}, verify=False)

        self.XTM_TOKEN = response.json().get('Token', None)
        user_info = response.json().get('User', None)
        if user_info:
            self.tenant_id = user_info.get('TenantID', None)

        self.request_header["Authorization"] = 'Bearer %s' % self.XTM_TOKEN
        return response.status_code

    def get_compute_profile_list(self, query_str=""):
        """
        Gets the profile list from xstream
        :return: json of profiles as list
        """
        profile_list = []
        if self.authenticate() == 200:
            filter_query = "?$filter="
            if self.tenant_id:
                filter_query += "TenantID eq '" + self.tenant_id + "'"
            if query_str:
                filter_query += "and " + query_str
            response = requests.get(self.url("profile" + filter_query),
                                    headers=self.request_header,
                                    verify=False)
            profile_list = response.json()
        else:
            print("Authentication Failed")
        return profile_list

    def get_disk_list(self, query_str=""):
        """
        Gets the disk list from xstream
        :return: json of disks as list
        """
        disk_list = []
        if self.authenticate() == 200:
            filter_query = "?$filter="
            if self.tenant_id:
                filter_query += "TenantID eq '" + self.tenant_id + "'"
            if query_str:
                filter_query += "and " + query_str
            response = requests.get(self.url("IsoFile" + filter_query), headers=self.request_header,
                                    verify=False)
            disk_list = response.json()
        else:
            print("Authentication Failed")
        for each_disk in disk_list:
            each_disk["FilePath"] = each_disk["FilePath"].split('/')[-1]
        return disk_list

    def get_site_list(self):
        site_list = []
        if self.authenticate() == 200:
            response = requests.get(self.url("Site"), headers=self.request_header, verify=False)
            site_list = response.json()
        else:
            print("Authentication Failed")

        return site_list

    def get_service_offering_list(self):
        service_offering_list = []
        if self.authenticate() == 200:
            response = requests.get(self.url("serviceoffering"), headers=self.request_header, verify=False)
            service_offering_list = response.json()
        else:
            print("Authentication Failed")
        return service_offering_list

    def get_hardware_templates_list(self):
        """
        Make REST call to xStream Portal to fetch
        Hardware Tmplate information.
        """
        hardware_templates_list = []
        if self.authenticate() == 200:
            response = requests.get(self.url("HardwareTemplate"),
                                    headers=self.request_header, verify=False)
            hardware_templates_list = response.json()
        return hardware_templates_list

    def get_network_list(self):
        """
        Make REST call to xStream Portal to fetch
        network information.
        """
        network_list = []
        if self.authenticate() == 200:
            response = requests.get(self.url("NetworkResource"),
                                    headers=self.request_header, verify=False)
            network_list = response.json()
        return network_list

    def get_template_list(self, vm_tmp_id=None):
        """
        Gets the policy list from repository
        :return: json of policies as list

        example VM Template from xStream

            {
              'OS': 'centos64Guest',
              'Timestamp': '2018-04-24T10:51:15.84Z',
              'Guest': {
                'Networks': [
                  {
                    'Network': 'VLAN_221',
                    'DeviceConfigId': 4000,
                    'MacAddress': '00:50:56:84:91:5e'
                  }
                ],
                'ToolsStatus': 'toolsNotInstalled',
                'ToolsRunningStatus': 'guestToolsNotRunning',
                'GuestState': 'notRunning',
                'ToolsVersionStatus': 'guestToolsNotInstalled',
                'GuestFullName': 'CentOS 4/5/6/7 (64-bit)'
              },
              'ExternalIdentifier': 'vm-62',
              'Hypervisor': {
                'Acl': [
                  {
                    'UserGroup': '77922643-80cb-7eb5-d6ca-6c21327b6d11',
                    'ResourceRole': '3985741b-0df2-4e9a-869b-46369842b0da',
                    'Permissions': 1
                  },
                  {
                    'UserGroup': '84e201ba-a318-46a9-abec-65c801d76477',
                    'ResourceRole': '3f9d5bf4-0f63-4ede-8a31-f832af8dc07b',
                    'Permissions': 2147483647
                  },
                  {
                    'UserGroup': '2819972e-7be9-4d7c-a809-cd1c6a1baf86',
                    'ResourceRole': 'ecb6d3ae-1ac8-46db-8206-3b2bf7e04714',
                    'Permissions': 1
                  },
                  {
                    'UserGroup': 'b742a2b9-2063-f1b0-b831-40aa5d39234e',
                    'ResourceRole': '3985741b-0df2-4e9a-869b-46369842b0da',
                    'Permissions': 1
                  }
                ],
                'Code': '1',
                'HypervisorID': '792a6466-d3bd-4a1e-809c-f5afe0464967',
                'TenantID': '9f92203e-313c-4b35-88ff-ff00a9d77153',
                'DriverID': '26a5d3fb-727f-c50d-effc-90ea7aee1a4a',
                'Name': 'TEST-SITE1',
                'Type': 'vCenter',
                'Site': {
                  'Settings': {
                    'AllowCpuRamAdjust': 'True',
                    'VSphere.RenameResourceOnAssignment': 'False',
                    'Storage.SupportedProvisioningTypes': 'Thin',
                    'Storage.IsolationLevel': '2',
                    'Rid.CountryCode': 'US',
                    'Authentication.Endpoint': 'https://10.100.26.90/api/v1.3/auth?invalidCert=true',
                    'DisableStorageAlarmEmails': 'False',
                    'Rid.LocationCode': '01'
                  },
                  'Code': '1',
                  'TenantID': '9f92203e-313c-4b35-88ff-ff00a9d77153',
                  'Region': {
                    'RegionID': '2fc9cfed-faad-6f54-acc3-8d13be55d60e',
                    'Active': True,
                    'Code': '1',
                    'Name': 'US',
                    'TenantID': '9f92203e-313c-4b35-88ff-ff00a9d77153'
                  },
                  'Name': 'Durham02',
                  'Active': True,
                  'SiteID': '69d29e4b-ce66-66b9-a07d-c4612616bb0f',
                  'Topology': 2
                }
              },
              'PowerState': 'poweredOff',
              'Disks': [
                {
                  'DeviceKey': 2000,
                  'CapacityKB': 16777216,
                  'StorageIdentifier': 'datastore-12',
                  'VirtualMachineDiskID': '61b8f1ab-c935-d85a-b00e-312ec1b0a52a',
                  'DiskMode': 5,
                  'UnitNumber': 0,
                  'ControllerKey': 1000,
                  'DiskFileName': '[5TBDatastore] NewVMtemplate/NewVMtemplate.vmdk',
                  'StorageID': '44739f0e-3dca-114d-5b33-d6229c00dd01',
                  'StorageProfileID': 'dbaf6e0f-4d54-4245-9506-8d63ad84151e',
                  'ControllerBusNumber': 0
                }
              ],
              'OSFullName': 'CentOS 4/5/6/7 (64-bit)',
              'IsTemplate': True,
              'NumNic': 1,
              'ParentHost': 'host-10',
              'StorageCapacityUsedMB': 1141,
              'HypervisorToolsStatus': 'toolsNotInstalled',
              'NumVirtualDisk': 1,
              'CpuHotAddEnabled': False,
              'ManagedResourceType': 'VirtualMachine',
              'UniqueId': '5004cf9d-26a8-fdc3-c473-7c8a742a8425',
              'Nics': [
                {
                  'VirtualMachineNicID': '22d230ce-cbc5-eae8-9dde-712aa9a8da23',
                  'NetworkID': '370531ee-7bad-d9fc-23c8-f3a302b9ed7c',
                  'NetworkIdentifier': 'network-13',
                  'DeviceKey': 4000,
                  'MacAddress': '00:50:56:84:91:5e',
                  'AdapterType': 4
                }
              ],
              'Description': '',
              'Cdroms': [
                {
                  'DeviceKey': 3002,
                  'FileSizeKB': -1,
                  'VirtualMachineCdromID': '66e848dc-708a-480b-b6b6-7f92da60be97',
                  'UnitNumber': 0,
                  'ControllerKey': 201,
                  'StorageIdentifier': 'datastore-11',
                  'StorageProfileID': '40aee1c1-13a9-46ea-81c7-ca91e7f96247',
                  'StorageID': '9f599888-ce9b-6ca9-9d22-b19790c0f9fa'
                }
              ],
              'RamAllocatedMB': 2048,
              'TenantID': '9f92203e-313c-4b35-88ff-ff00a9d77153',
              'CpuShares': 1000,
              'NumCpu': 1,
              'ResourceGroups': [
                'All Resources',
                'Unassigned',
                'All Virtual Machines and Templates'
              ],
              'StorageCapacityUsedPc': 6,
              'CpuHotRemoveEnabled': False,
              'MemoryHotAddEnabled': False,
              'StorageCapacityAllocatedMB': 18594,
              'Name': 'NewVMtemplate',
              'VirtualMachineID': '1ad4a1e7-cc00-c091-c007-d6ae9f54c754',
              'Acl': [
                {
                  'UserGroup': '84e201ba-a318-46a9-abec-65c801d76477',
                  'ResourceRole': '3f9d5bf4-0f63-4ede-8a31-f832af8dc07b',
                  'Permissions': 2147483647
                },
                {
                  'UserGroup': '77922643-80cb-7eb5-d6ca-6c21327b6d11',
                  'ResourceRole': 'b690f28c-287c-4962-95de-3c66dc35ec4f',
                  'Permissions': 2147483647
                }
              ],
              'CustomerDefinedName': 'NewVMtemplate',
              'CpuLimitMHz': -1,
              'RamShares': 20480
            }
        """
        template_list = []
        if self.authenticate() == 200:
            filter_query = "?$filter=IsTemplate eq true"
            if vm_tmp_id:
                filter_query = filter_query + " and VirtualMachineID eq '" + vm_tmp_id + "'"
            if self.tenant_id:
                filter_query = filter_query + " and TenantID eq '" + self.tenant_id + "'"
            response = requests.get(self.url("VirtualMachine" + filter_query),
                                    headers=self.request_header, verify=False)
            template_list = response.json()
        return template_list


    def get_compute_allocation(self):
        compute_allocation = []
        if self.authenticate() == 200:
            filter_query = "?$filter=AllocationTenantID eq '" + self.tenant_id + "'"
#            filter_query = filter_query + "and SiteID eq  '" + site_id + "'"
            response = requests.get(self.url("ServiceAllocation" + filter_query),
                                    headers=self.request_header, verify=False)
            compute_allocation = response.json()
        return compute_allocation


    def get_task_status(self, message_id):
        """
        Gets the request status using TaskInfo API

        :param message_id:
        :return: status
        """
        '''
        example json for taskinfo
        {
            'ManagedResourceID': '9f92203e-313c-4b35-88ff-ff00a9d77153', 'ParentTaskId': None,
            'TenantID': '9f92203e-313c-4b35-88ff-ff00a9d77153', 'CreatedDate': '2018-06-22T05:28:19.777Z',
            'SessionID': None, 'EditedBy': '1a@VSFL.LAB', 'PortalUserName': '1a@VSFL.LAB', 'MessageName': 'SetVM',
            'TaskInfoID': 'c22135d9-5931-4aff-8462-e6601c5b573b', 'LocalizableError': None, 'CreatedBy': '1a@VSFL.LAB',
            'ManagedResourceName': 'qqqqqq', 'Errors': None, 'TaskName': 'Provisioning VM qqqqqq', 'Progress': 1,
            'Cancellable': False, 'StateMessage': 'Running', 'StartTime': '2018-06-22T05:28:19.777Z',
            'CorrelationId': 'c22135d9-5931-4aff-8462-e6601c5b573b', 'Result': None, 'EditedDate': '2018-06-22T05:28:20.919Z',
            'ManagedResourceIdentifier': None, 'ManagedResourceType': 'Tenant', 'CustomerId': 0,
            'TaskId': 'c22135d9-5931-4aff-8462-e6601c5b573b', 'SiteID': '69d29e4b-ce66-66b9-a07d-c4612616bb0f',
            'FinishTime': None, 'HypervisorID': None, 'UserName': '1a@VSFL.LAB',
            'Acl': [{'ResourceRole': '3f9d5bf4-0f63-4ede-8a31-f832af8dc07b',
            'UserGroup': '77922643-80cb-7eb5-d6ca-6c21327b6d11', 'Permissions': 1},
            {'ResourceRole': '3985741b-0df2-4e9a-869b-46369842b0da',
            'UserGroup': 'b742a2b9-2063-f1b0-b831-40aa5d39234e', 'Permissions': 1},
            {'ResourceRole': '3f9d5bf4-0f63-4ede-8a31-f832af8dc07b',
            'UserGroup': '84e201ba-a318-46a9-abec-65c801d76477', 'Permissions': 1},
            {'ResourceRole': '3f9d5bf4-0f63-4ede-8a31-f832af8dc07b',
            'UserGroup': '2819972e-7be9-4d7c-a809-cd1c6a1baf86', 'Permissions': 1}],
            'State': 3
        }
        '''

        if self.authenticate() == 200:
            task_completed = False
            StateMessage = "Queued"
            ReturnData= {"state": "Error"}
            while not task_completed:
                sleep(WAIT_TIME_BETWEEN_REQUESTS)
                response = requests.get(self.url("TaskInfo" + "/" + str(message_id)),
                                     headers=self.request_header, verify=False)
                if 'StateMessage' in response.json():
                    StateMessage = response.json()['StateMessage']
                if StateMessage == "Success" or StateMessage == "Error":
                    task_completed = True
                    ReturnData["state"] = StateMessage
                    if StateMessage == "Success": 
                        ReturnData["vm_id"] = response.json()['Result'] 

        return ReturnData 

    def get_vm_info(self, vm_id):
        """
       Fetch VM information from Virtual Machine ID 

        :param vm_id:
        :return: VM Details
        """
        if self.authenticate() == 200:
            task_completed = False
            VM_details = {} 
            response = requests.get(self.url("VirtualMachine" + "/" + str(vm_id)),
                                 headers=self.request_header, verify=False)
            VM_details = response.json()

        return VM_details
