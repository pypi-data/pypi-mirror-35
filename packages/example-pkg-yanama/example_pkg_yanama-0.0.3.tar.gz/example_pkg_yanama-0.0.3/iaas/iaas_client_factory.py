import yaml


def load_yml_file(config_file):
    """
    return data from yml file
    param:
      config_file: path of yml file
    return_value:
      will return loaded_data in dictonary format
    """
    try:
        p_file = open(config_file, "r+")
        loaded_data = yaml.load(p_file)
        p_file.close()
    except Exception as ex:
        template = "Exception: An exception of type {0} occured: {1}"
        message = template.format(type(ex).__name__, str(ex))
        raise Exception(message)

    return loaded_data


#
# # End of load_yml_file()


def get_yml_data(config_file, key):
    """
    This functino will return data in the form of dictionary for given key from config_file
    param:
      config_file: path of yml file
      key: name of the key from config_file
    return_value:
      will return value for given key [in dictonary format]
    """
    loaded_data = load_yml_file(config_file)

    try:
        data = dict(loaded_data)
        for item in data.keys():
            if data[item].__contains__(key):
                print('API client for method {}: {}'.format(key, item))
                return item

    except Exception as ex:
        template = "Exception: An exception of type {0} occured: {1}"
        message = template.format(type(ex).__name__, str(ex))
        raise Exception(message)


#
# # End of get_yml_data()

class APIClientFactory:
    class Xstream:
        def create_vm(self):
            return "XStream :VM Created Successfully"

    class Chpapi:
        def delete_vm(self):
            return "CHPAPI :VM Deleted Successfully"

    @staticmethod
    def create_api_client(api_client):
        get_class = getattr(APIClientFactory, api_client)
        instance_class = get_class()
        return instance_class


def execute(api_method):
    api_client = get_yml_data("api_config.yaml" , api_method)
    factory_instance = APIClientFactory.create_api_client(api_client)
    execute_method = getattr(factory_instance, api_method)
    print(execute_method())


execute("create_vm")
execute("delete_vm")
