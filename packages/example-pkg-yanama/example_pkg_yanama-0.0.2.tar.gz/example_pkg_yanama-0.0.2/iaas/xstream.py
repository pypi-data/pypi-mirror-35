import requests
from vec import Xstream


class XstreamClass():
    def __init__(self):
        pass

    def create_tenant(self):
        ## TODO: Discuss and Implement.
        raise NotImplementedError("To be implemented")
        return

    def create_user(self):
        ## TODO: Discuss and Implement.
        raise NotImplementedError("To be implemented")
        return

    def create_vm(self, post_data_dic):
        #if "CustomerDefinedName" in post_data_dic and check_vm_name_exists(post_data_dic["CustomerDefinedName"]) is True:
        #    print("Error: VM with this "+post_data_dic['CustomerDefinedName']+" already exists!!!")
        #    return 0

        xstream = Xstream()
        if xstream.authenticate() == 200:
            state={}
            post_data_dic["TenantID"] = xstream.tenant_id
            response = requests.post(xstream.url("VirtualMachine/SetVM"),
                                     headers=xstream.request_header,
                                     json=post_data_dic,
                                     verify=False)

            response_json = response.json() # {'Headers': {'MessageId': '<guid>'}, 'Status': 'Queued'}
            if 'Headers' in response_json and 'MessageId' in response_json['Headers']:
                state = xstream.get_task_status(response_json['Headers']['MessageId'])
                return state 
        return False

    def create_storage(self):
        ## TODO: Discuss and Implement.
        raise NotImplementedError("To be implemented")
        return

    def create_network(self):
        ## TODO: Discuss and Implement.
        raise NotImplementedError("To be implemented")
        return

    def create_compute(self):
        ## TODO: Discuss and Implement.
        raise NotImplementedError("To be implemented")
        return

    def assign_network_to_tenant(self):
        ## TODO: Discuss and Implement.
        raise NotImplementedError("To be implemented")
        return

    def assign_storage_to_tenant(self):
        ## TODO: Discuss and Implement.
        raise NotImplementedError("To be implemented")
        return

    def assign_compute_to_tenant(self):
        ## TODO: Discuss and Implement.
        raise NotImplementedError("To be implemented")
        return

    def populate_network_for_all(self):
        ## TODO: Discuss and Implement.
        raise NotImplementedError("To be implemented")
        return

