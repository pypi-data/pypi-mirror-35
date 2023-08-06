import sys, os
import json
import requests
from datetime import datetime
import threading
import Queue
from deepdiff import DeepDiff
import re

class IWSClient:

    _tmp_directory = ""
    _configfile = _tmp_directory + "config.json"
    _output =  _tmp_directory + "output"
    _api_url =  "https://api.evolve.threatintelligence.com/"
    _file_object_exists = False
    _signed_endpoint =  "hawking/getsignedurl"
    _list_file_endpoint =  "hawking/listfile"
    _log_event_endpoint =  "event/create"
    _signed_url_put_method = "put_object"
    _signed_url_get_method = "get_object"
    _content_type = "application/octet-stream"
    _already_scan_filename = "state"
    _already_scan_file_content = None
    _state_version = "1.0.0.3"
    _state_known_versions = [ "1.0" ]
    config = {}

    ### Iws Queue references ##
    _queue_in      = None  # input commands to run on threads
    _queue_out     = None  # output from command run on threads
    _queue_tag     = '**IWS-QUEUE-TAG**'  # tag to place on queue to signal thread to finish
    _threads       = []    # thread pool
    _threads_max   = 10    # thread pool size limit
    _thread_target = None  # thread pool target function

    _commands = {
                "container-ls" : { "endpoint": "hawking/list", "operation": "list"},
                "container-create" : { "endpoint": "hawking/create", "operation": "create"},
                "container-delete" : { "endpoint": "hawking/delete", "operation": "delete"},
                "container-update" : { "endpoint": "hawking/update", "operation": "update"},
                "container-ls-files" : { "endpoint": "hawking/list", "operation": "list_file"},
                "module-ls" : { "endpoint": "module/list", "operation": "list"},
                "module-delete" : { "endpoint": "module/delete", "operation": "delete"},
                "module-describe" : { "endpoint": "module/getitem", "operation": "get_item"},
                "moduleinstance-ls" : { "endpoint": "moduleinstance/list", "operation": "list"},
                "moduleinstance-describe" : { "endpoint": "moduleinstance/getitem", "operation": "get_item"},
                "moduleinstance-create" : { "endpoint": "moduleinstance/create", "operation": "create"},
                "moduleinstance-delete" : { "endpoint": "moduleinstance/delete", "operation": "delete"},
                "moduleinstance-invoke" : { "endpoint": "moduleinstance/invoke", "operation": "invoke"},
                "workflow-ls" : { "endpoint": "workflow/list", "operation": "list"},
                "workflow-create" : { "endpoint": "workflow/create", "operation": "create"},
                "workflow-delete" : { "endpoint": "workflow/delete", "operation": "delete"},
                "workflow-describe" : { "endpoint": "workflow/getitem", "operation": "get_item"},
                "workflowinstance-ls" : { "endpoint": "workflowinstance/list", "operation": "list"},
                "workflowinstance-create" : { "endpoint": "workflowinstance/create", "operation": "create"},
                "workflowinstance-delete" : { "endpoint": "workflowinstance/delete", "operation": "delete"},
                "workflowinstance-describe" : { "endpoint": "workflowinstance/getitem", "operation": "get_item"},
                "workflowinstance-messages" : { "endpoint": "workflowinstance/messages", "operation": "messages"},
                "workflowinstance-listresource" : { "endpoint": "workflowinstance/listresource", "operation": "list_resources"},
                "securityzone-ls" : { "endpoint": "cluster/list", "operation": "list"},
                "securityzone-describe" : { "endpoint": "cluster/getitem", "operation": "get_item"},
                "securityzone-ls-tasks" : { "endpoint": "cluster/list", "operation": "list_task"},
                "securityzone-create" : { "endpoint": "cluster/create", "operation": "create"},
                "share-ls" : { "endpoint": "share/list", "operation": "list"},
                "share-create" : { "endpoint": "share/create", "operation": "create"},
                "share-delete" : { "endpoint": "share/delete", "operation": "delete"},
                "share-import" : { "endpoint": "share/import", "operation": "import"},
                "share-import-ls" : { "endpoint": "share/list", "operation": "import_list"},
                "share-getitem" : { "endpoint": "share/list", "operation": "get_item"},
                "event-ls" : { "endpoint": "event/list", "operation": "list"},
                "event-messages" : { "endpoint": "event/messages", "operation": "messages"},
                "dashboard-ls" : { "endpoint": "dashboard/list", "operation": "list"},
                "dashboard-delete" : { "endpoint": "dashboard/delete", "operation": "delete"},
                "dashboard-describe" : { "endpoint": "dashboard/getitem", "operation": "get_item"},
                "agent-ls" : { "endpoint": "agent/list", "operation": "list"},
                "agent-create" : { "endpoint": "agent/create", "operation": "create"},
                "agent-package" : { "endpoint": "agent/package", "operation": "package"},
                "agent-delete" : { "endpoint": "agent/delete", "operation": "delete"},
                "agent-device-register" : { "endpoint": "agent/device/register", "operation": "register"},
                "agent-device-downloadmodule" : { "endpoint": "agent/device/downloadmodule", "operation": "downloadmodule"},
                "agent-device-downloaddata" : { "endpoint": "agent/device/downloaddata", "operation": "downloaddata"},
                "agent-device-uploaddata" : { "endpoint": "agent/device/uploaddata", "operation": "uploaddata"},
                "agent-device-messages" : { "endpoint": "agent/device/messages", "operation": "messages"},
                "agent-device-updateconfig" : { "endpoint": "agent/device/updateconfig", "operation": "updateconfig"},
                "agent-device-list" : { "endpoint": "agent/device/list", "operation": "list"},
                "agent-device-file-metadata" : { "endpoint": "agent/device/list", "operation": "get_file_meta"},
                "agent-device-logevent" : { "endpoint": "agent/device/logevent", "operation": "log_event"},
                "agent-describe" : { "endpoint": "agent/list", "operation": "get_item"}
                }

    def __init__(self, **kwargs):

        config_file_path = self._configfile
        if 'ConfigFile' in kwargs:
           config_file_path = kwargs['ConfigFile']

        if os.path.isfile(config_file_path):
            if os.stat(config_file_path).st_size > 0:
                with open(config_file_path, 'r') as f:
                    self.config =  json.load(f)
                    return

    def get_state(self, **kwargs):

        if not "ContainerId" in kwargs:
            sys.exit("Error: Missing Parameter (ContainerId)")

        if not "Row" in kwargs:
            sys.exit("Error: Missing Parameter (Row)")

        if not self._already_scan_file_content:
            self._already_scan_file_content = self.get_file(ContainerId=kwargs['ContainerId'], FileName=self._already_scan_filename)

        # no state, then agreed row is unique
        if not self._already_scan_file_content:
            return False

        # sorting a text file?
        if type(kwargs['Row']) is str:

            item = kwargs['Row'].strip()

            if self._already_scan_file_content.find(item) == -1:
                return False
            else:
                return True

        # sorting a structured file?
        elif type(kwargs['Row']) is list or type(kwargs['Row']) is dict:

            item = kwargs['Row']

            if not self._already_scan_file_content:
                self._already_scan_file_content = self.get_file(ContainerId=kwargs['ContainerId'], FileName=self._already_scan_filename)

            if not self._already_scan_file_content:
                return False

            state_data = json.loads(self._already_scan_file_content)
            for state_idx, state_element in enumerate(state_data):
                ddiff = DeepDiff(state_element, item)
                if not ddiff:
                    return True
            return False

    def set_state(self, **kwargs):

        if not "ContainerId" in kwargs:
            sys.exit("Error: Missing Parameter (ContainerId)")

        if not "State" in kwargs:
            sys.exit("Error: Missing Parameter (State)")

        if type(kwargs['State']) is str:

            if self._already_scan_file_content:
                self._already_scan_file_content += "\n" + kwargs['State']
            else:
                self._already_scan_file_content = kwargs['State']

            self.upload_file(ContainerId=kwargs['ContainerId'], FileName=self._already_scan_filename, Content=self._already_scan_file_content)

        elif type(kwargs['State']) is list or type(kwargs['State']) is dict:

            if not self._already_scan_file_content:
                self._already_scan_file_content = self.get_file(ContainerId=kwargs['ContainerId'], FileName=self._already_scan_filename)

            # empty state, set it up
            if not self._already_scan_file_content:
                state_data = []
                self._already_scan_file_content = json.dumps(state_data)

            # rehydrate state_data
            state_data = json.loads(self._already_scan_file_content)

            # If it's "Bulk" then this is a list of data elements that are each to be appended as stand-alone blocks
            # i.e. add the element_list item to the list; list[n+1] = element_list[0] ...
            if "Bulk" in kwargs and kwargs["Bulk"] is True:
                for state_idx, state_item in enumerate(kwargs['State']):
                    state_data.append(state_item)

            # If it's *not* "Bulk" then we want the element appended as a single block grouping a pre-determined subset/relationship
            # i.e. add the element_list to the list; list[n+1] = element_list
            else:
                state_data.append(kwargs['State'])

            # squish n store
            self._already_scan_file_content = json.dumps(state_data)
            self.upload_file(ContainerId=kwargs['ContainerId'], FileName=self._already_scan_filename, Content=self._already_scan_file_content)

    def reset_state(self, **kwargs):
        if "ContainerId" in kwargs:
            self._already_scan_file_content = ""
            self.upload_file(ContainerId=kwargs['ContainerId'], FileName=self._already_scan_filename, Content=self._already_scan_file_content)
        else:
            sys.exit("Error: Missing Parameter (ContainerId)")

    def pullfrom_state(self, **kwargs):
        # def pullkey(obj, path, option=None):
        if not "State" in kwargs:
            sys.exit("Error: Missing Parameter (Obj)")
        if not "Path" in kwargs:
            sys.exit("Error: Missing Parameter (Path)")

        obj = kwargs['State']
        path = kwargs['Path']

        err = None
        if "Error" in kwargs:
            err = kwargs["Error"]

        find_first = None
        find_each = None
        find_first_option = "First"
        find_each_option = "Each"
        option = None
        if "Option" in kwargs:
            option = kwargs["Option"]
            if option == find_first_option:
                find_first = True
            elif option == find_each_option:
                find_each = True

        # path to list
        if not isinstance(path, list):
            if not len(path):
                return err
            path = path.replace("/", ".*.")
            path = path.replace("*", "")
            #path = path.strip('.')
            path = path.split('.')

        # exit if last element
        if not path:
            if isinstance(obj, list):
                if not len(obj):
                    return err
                if len(obj) == 1:
                    return obj[0]
            return obj

        # recurse if not
        key = path[0]
        wild_search = False
        if key is "":
            wild_search = True
        path.pop(0)

        # recursion shares references
        local_path = path[:]
        local_key = key[:]

        if isinstance(obj, dict):
            if not wild_search:
                # Find specific
                if len(local_key) == 0:
                    return err
                if not local_key in obj:
                    return err
                # val = pullkey(obj[local_key], local_path, option)
                val = self.pullfrom_state(State=obj[local_key], Path=local_path, Option=option, Error=err)
            else:
                # Wild, find first
                if find_first:
                    for key in obj:
                        # val = pullkey(obj[key], local_path, option)
                        val = self.pullfrom_state(State=obj[key], Path=local_path, Option=option, Error=err)
                        if val is not err:
                            break
                # Wild, find each
                elif find_each:
                    val = []
                    for key in obj:
                        local_path = path[:]
                        # this_val = pullkey(obj[key], local_path, option)
                        this_val = self.pullfrom_state(State=obj[key], Path=local_path, Option=option, Error=err)
                        if this_val is not err:
                            if len(this_val):
                                val.append(this_val)
                    if not len(val):
                        val = None
                    if len(val) == 1:
                        val = val[0]
                else:
                    return err
        elif isinstance(obj, list):
            if not wild_search:
                # Find specific
                if len(local_key) == 0:
                    return err
                if not local_key.isdigit():
                    return err
                idx = int(local_key, 10)
                if idx >= len(obj):
                    return err
                # val = pullkey(obj[idx], local_path, option)
                val = self.pullfrom_state(State=obj[idx], Path=local_path, Option=option, Error=err)
            else:
                # Wild, find first
                if find_first:
                    for idx in range(len(obj)):
                        # val = pullkey(obj[idx], local_path, option)
                        val = self.pullfrom_state(State=obj[idx], Path=local_path, Option=option, Error=err)
                        if val is not err:
                            break
                # Wild, find each
                elif find_each:
                    val = []
                    for idx in range(len(obj)):
                        local_path = path[:]
                        # this_val = pullkey(obj[idx], local_path, option)
                        this_val = self.pullfrom_state(State=obj[idx], Path=local_path, Option=option, Error=err)
                        if this_val is not err:
                            if len(this_val):
                                val.append(this_val)
                    if not len(val):
                        val = None
                    if len(val) == 1:
                        val = val[0]
                else:
                    return err
        else:
            # Exception .. reached end early
            if len(local_path) > 0:
                return err
            return obj
        return val

    def format_state(self, **kwargs):

        if not "Format" in kwargs:
            sys.exit("Error: Missing Parameter (Format)")

        if not "State" in kwargs:
            sys.exit("Error: Missing Parameter (State)")

        if type(kwargs['Format']) is not str:
            sys.exit("Error: Parameter is wrong type (Format)")

        if type(kwargs['State']) is not list and type(kwargs['State']) is not dict:
            sys.exit("Error: Parameter is wrong type (State)")

        format_file = None
        if "FormatFile" in kwargs:
            if type(kwargs['FormatFile']) is not str:
                sys.exit("Error: Parameter is wrong type (FormatFile)")
            format_file = kwargs['FormatFile']

        # translations = { '{one_field_to_many}': [ 'priority_field', 'secondary_field', 'tertiary_field' ], '{one_field_to_one}': 'one_field_name' }
        translations = { '{meta_host}': [ 'ipv4', 'hostname', 'ipv6' ] }

        if "Translations" in kwargs:
            if kwargs['Translations'] is None:
                translations = None
            elif type(kwargs['Translations']) is not dict:
                sys.exit("Error: Parameter is wrong type (Translations)")
            else:
                translations = kwargs['Translations']

        format_data = ""
        # Walk the state
        for idx, dictionary in enumerate(kwargs['State']):
            # template = '{service}://{host}:{port}/\n'
            template = kwargs['Format']
            # Apply dictionary to template
            for key in dictionary:
                if not str("{" + key + "}") in template:
                    continue
                if not isinstance(dictionary[key], basestring):
                    continue
                template = template.replace(str("{" + key + "}"), dictionary[key])
            # Apply translations to dictionary to template
            if translations is not None:
                for key in translations:
                    if not key in template:
                        continue
                    if type(translations[key]) is list:
                        substitutes = translations[key]
                        for idx, tkey in enumerate(substitutes):
                            if not tkey in dictionary:
                                continue
                            template = template.replace(str(key), dictionary[str(tkey)])
                    else:
                        tkey = translations[key]
                        if not tkey in dictionary:
                            continue
                        template = template.replace(str(key), dictionary[str(tkey)])
            format_data += template

        if format_file:
            with open(format_file, "w") as out_file:
                out_file.write(format_data)

        return format_data

    def version_state(self, **kwargs):

        ver = self._state_version
        if "Version" in kwargs:
            if type(kwargs['Version']) is not str:
                sys.exit("Error: Parameter is wrong type (Version)")
            ver = kwargs['Version']

        # Version Check i.e. n.n.n.n
        ver_array = re.findall(r"\d+",ver)
        if not len(ver_array) >= 2 and len(ver_array) <= 4:
            sys.exit("Error: Parameter is wrong type (Version)")

        mm_ver = str(ver_array[0]) + "." + str(ver_array[1])
        for idx,version in enumerate(self._state_known_versions):
            if mm_ver == version:
                return version

        return None

    def read_state(self, **kwargs):

        if not "StateFile" in kwargs:
            sys.exit("Error: Missing Parameter (StateFile)")

        if type(kwargs['StateFile']) is not str:
            sys.exit("Error: Parameter is wrong type (StateFile)")

        if "Version" in kwargs:
            version = self.version_state(Version=kwargs["Version"])
            if version is None:
                sys.exit("Error: Version is incompatible Major.Minor value")

        state_file = kwargs['StateFile']
        if not os.path.exists(state_file):
            sys.exit("Error: File does not exist (StateFile)")

        file_content = ""
        with open(state_file, "r") as in_file:
            file_content = in_file.read()

        state_data = json.loads(file_content)
        return state_data

    def write_state(self, **kwargs):

        if not "StateFile" in kwargs:
            sys.exit("Error: Missing Parameter (StateFile)")

        if not "State" in kwargs:
            sys.exit("Error: Missing Parameter (State)")

        if type(kwargs['StateFile']) is not str:
            sys.exit("Error: Parameter is wrong type (StateFile)")

        if type(kwargs['State']) is not list and type(kwargs['State']) is not dict:
            sys.exit("Error: Parameter is wrong type (State)")

        if "Version" in kwargs:
            version = self.version_state(Version=kwargs["Version"])
            if version is None:
                sys.exit("Error: Version is incompatible Major.Minor value")

        state_file = kwargs['StateFile']
        state_data = []

        # need to re-implement non-bulk state file work (i.e. re-read the file and write the deltas)

            # if not self._already_scan_file_content:
                # self._already_scan_file_content = self.get_file(ContainerId=kwargs['ContainerId'], FileName=self._already_scan_filename)

            # empty state, set it up
            # if not self._already_scan_file_content:
                # state_data = []
                # self._already_scan_file_content = json.dumps(state_data)

            # rehydrate state_data
            # state_data = json.loads(self._already_scan_file_content)

        # If it's "Bulk" then this is a list of data elements that are each to be appended as stand-alone blocks
        # i.e. add the element_list item to the list; list[n+1] = element_list[0] ...
        # if "Bulk" in kwargs and kwargs["Bulk"] is True:
        #     for state_idx, state_item in enumerate(kwargs['State']):
        #         state_data.append(state_item)

        # If it's *not* "Bulk" then we want the element appended as a single block grouping a pre-determined subset/relationship
        # i.e. add the element_list to the list; list[n+1] = element_list
        # else:
        #     state_data.append(kwargs['State'])

        # temporary state management
        state_data = kwargs["State"]
        state_data["version"] = version

        # squish n store
        file_content = json.dumps(state_data)
        with open(state_file, "a") as out_file:
            out_file.write(file_content)

        return True

    def set_utc_datetime(self):
        return str(datetime.utcnow().isoformat('T'))

    def get_container(self, index='All'):

        if "containers" in self.config:
            if index < len(self.config["containers"]):
                return self.config["containers"][index]["id"]
            else:
                if "containers" in self.config:
                    return self.config["containers"]

        return False

    def get_file_object_key(self):

        if "file_object_key" in self.config:
            return self.config["file_object_key"]

        return False

    def add_to_output(self, **kwargs):

        if "FileName" in kwargs and "FileContent" in kwargs:
            #directory_path = os.path.join(os.getcwd(), self._output)
            directory_path = self._output
            self._check_directory_exists(directory_path)
            name, extension = os.path.splitext(kwargs['FileName'])
            filename = name + "_" + self.set_utc_datetime() + extension
            file_object = os.path.join(directory_path, filename)
            fwh = open(file_object,'w')
            fwh.write(kwargs['FileContent']);
            fwh.close()
        else:
            sys.exit("Error: Missing Parameter")

    def get_file(self, **kwargs):

        #size = kwargs.get('size', None)
        container_id = False
        filename = False

        if "ObjectKey" in kwargs:
            objectkey = kwargs['ObjectKey']
            objectkey_array = objectkey.split("/")
            container_id = objectkey_array[0]
            filename = objectkey_array[1]

        else:
            if "ContainerId" not in kwargs or "FileName" not in kwargs:
                sys.exit('Error: Invalid parameters, check container_id and filename')
            else:
                container_id = kwargs['ContainerId']
                filename = kwargs['FileName']

        if container_id and filename:
            size = None

            container_dir = container_id
            if 'ContainerName' in kwargs:
                container_dir = kwargs['ContainerName'].replace(" ", "_") + "_" + container_id

            self._check_file_object_exist(container_dir, filename)

            if not self._file_object_exists:
                self._download_file(container_id, filename)

            return self.read_file()

    def read_file(self):

        frh = open(self.file_object, "r")
        file_content = frh.read();
        frh.close()

        if '<Error><Code>NoSuchKey</Code>' in file_content:
            file_content = ""

        return file_content.strip()

    def get_file_path(self, **kwargs):

        if "ObjectKey" in kwargs:
            objectkey = kwargs['ObjectKey']
            objectkey_array = objectkey.split("/")
            container_id = objectkey_array[0]
            filename = objectkey_array[1]

            self._check_file_object_exist(container_id, filename)
            if self._file_object_exists:
                return self.file_object

        sys.exit("Error: File Doesn't Exist")

    def _download_file(self, container_id, filename):

        if not self._file_object_exists:

            self._set_signedurl_filename(container_id, filename)
            #self._set_signedurl_contentype(content_type)
            self._set_signedurl_method(self._signed_url_get_method)

            api_response = self._get_signed_url()
            api_response_dict = json.loads(api_response.text)

            if "url" in api_response_dict:

                response = requests.get(api_response_dict["url"], stream=True)

                with open(self.file_object, 'wb') as fd:
                    for chunk in response.iter_content(chunk_size=1024):
                    #    if "<Code>NoSuchKey</Code>" in chunk:
                    #        return
                        fd.write(chunk)
                file_size = os.stat(self.file_object).st_size
                self.log_event(ResourceId=container_id, ResourceName=filename, EventType="11", FileSize=file_size)

                self._file_object_exists = True

        return

    def _check_file_object_exist(self, container_id, filename):

        #full_path = os.path.realpath(__file__)
        #path, class_file_name = os.path.split(full_path)
        path = self._tmp_directory
        directory_path = os.path.join(path, container_id)
        self.file_object = os.path.join(directory_path, filename)
        #print(self.file_object)

        self._check_directory_exists(directory_path)

        if "iws-system/" in filename:
            file_dir_path = os.path.join(directory_path, "iws-system/")
            self._check_directory_exists(file_dir_path)

        if os.path.exists(self.file_object):
            self._file_object_exists = True
        else:
            self._file_object_exists = False

        return

    def _check_directory_exists(self, directory_path):

        if not os.path.isdir(directory_path):
            os.mkdir(directory_path)

        return

    def upload_output(self, **kwargs):

        if "ContainerId" in kwargs:

            if os.path.isdir(self._output):
                for root, dirs, files in os.walk(self._output):
                    #print("root", root)
                    #print("dirs", dirs)
                    #print("files", files)
                    if files:
                        for name in files:
                            #print("filename: " + name)
                            file_object = root + "/" + name
                            #print(file_object)
                            s3_object_key = kwargs['ContainerId'] + file_object[len(self._output):]
                            #print(s3_object_key)
                            frh = open(file_object, "r")
                            file_content = frh.read();
                            #print(file_content)
                            self.upload_file(ObjectKey=s3_object_key, Content=file_content)
                            os.remove(file_object)
                            frh.close()

        return

    # Added on 22nd Nov but need to check options with Chris as he's writing client lib
    def _set_api_request_headers(self):

        if "agent_key" in self.config:
            authorization = "Bearer agentkey:" + str(self.config["agent_key"])
        else:
            authorization = "Bearer apikey:" + str(self.config["client_api_key"])

        self._api_request_headers = {"Authorization" : authorization, "Content-Type" : "application/json"}

    def _set_api_request_endpoint(self, endpoint):

        # Check Region Specific API URL; Mostly for PTConsole and IWSCLI
        if 'region' in self.config:

            api_url = self._api_url[self._api_url.find('api.'):]

            if self.config['region'] == "US":
                 self._api_url = "https://" + api_url
            else:
                self._api_url = "https://" + self.config['region'].lower() + "." + api_url

        self._api_request_endpoint = self._api_url + endpoint

    def _set_signedurl_filename(self, container_id, filename):
        self._api_request_data = {"operation": "getsignedurl", "payload" : {"Item":{}}}
        self._api_request_data["payload"]["Item"]["FileObjectKey"] = container_id + "/" + filename

    def _set_signedurl_contentype(self, content_type):
        self._api_request_data["payload"]["Item"]["ContentType"] = content_type

    def _set_signedurl_method(self, method):
        self._api_request_data["payload"]["Item"]["Method"] = method

    def _get_signed_url(self):
        self._set_api_request_endpoint(self._signed_endpoint)
        self._set_api_request_headers()
        api_response =  self._call_api()

        return api_response

    def _set_json_data(self, data):
        data = {"Records": [data] }
        return data
        #return json.dumps(data)

    def _call_api(self, setJsonData = True):

        if setJsonData:
            self._api_request_data = self._set_json_data(self._api_request_data)

        #print(self._api_request_endpoint,self._api_request_data,self._api_request_headers)
        response = requests.post(self._api_request_endpoint, json = self._api_request_data, headers=self._api_request_headers)
        #print(response.text)
        return response

    def upload_file(self, **kwargs):

        payload_response = {}
        payload_response['status'] = "error"

        if "ObjectKey" in kwargs and "Content" in kwargs:
            objectkey = kwargs['ObjectKey']
            objectkey_array = objectkey.split("/")
            container_id = objectkey_array[0]
            filename = objectkey_array[1]
        elif "ContainerId" in kwargs and "FileName" in kwargs and "Content" in kwargs:
            container_id = kwargs['ContainerId']
            filename = kwargs['FileName']
        else:
            print("Missing Required Argument")

        #self._api_request_data = {"operation": "getsignedurl", "payload" : {"Item":{}}}

        content_type =  self._content_type
        if "ContentType" in kwargs:
            content_type = kwargs['ContentType']

        self._set_signedurl_filename(container_id, filename)
        self._set_signedurl_contentype(content_type)
        self._set_signedurl_method(self._signed_url_put_method)

        api_response = self._get_signed_url()
        api_response_dict = json.loads(api_response.text)

        if "url" in api_response_dict:
            # upload content
            headers = {"Content-Type" : content_type}
            response = requests.put(api_response_dict["url"], data = kwargs['Content'], headers=headers)

            if response.status_code == 200:
                payload_response['status'] = "ok"

        return payload_response

    def list_files(self, **kwargs):

        if "ContainerId" not in kwargs:
            print("Missing Required Argument ContainerId in list_files")
            api_response_dict = False
        else:
            self._api_request_data = {"operation": "list_file","payload": {"Item": {"ContainerId": kwargs['ContainerId']}}}

            if "MaxResults" in kwargs:
                self._api_request_data["payload"]["Item"]["MaxResults"] = kwargs['MaxResults']

            if "OrderBy" in kwargs:
                self._api_request_data["payload"]["Item"]["OrderBy"] = kwargs['OrderBy']

            if "Key" in kwargs:
                self._api_request_data["payload"]["Item"]["Key"] = kwargs['Key']

            self._set_api_request_endpoint(self._list_file_endpoint)
            self._set_api_request_headers()
            api_response = self._call_api()
            api_response_dict = json.loads(api_response.text)

        return api_response_dict

    def thread(self, target, max_threads=10):
        """
        Enqueue a command to run on a thread
        """

        # setup queues if not already done
        if self._queue_in == None:
            self._queue_in = Queue.Queue()

        if self._queue_out == None:
            self._queue_out = Queue.Queue()

        # enqueue a command to run on thread
        self._thread_target = target
        self._threads_max = max_threads

    def run(self,param=()):
        """
        Enqueue a parameter to run on the thread pool
        """
        #global _queue_in

        # sanity check
        if self._queue_in == None:
            print '[!] Queue has not been initialised, was thread() run?'
            sys.exit(1)

        # enqueue parameter
        self._queue_in.put(param)

    def _thread_helper(self,target, iq, oq):
        """
        Loop over queue until empty
        """
        #global _queue_tag

        while True:
            params = iq.get()                   # pop an item off the queue

            if params == self._queue_tag:        # if value matches tag then return
                oq.put(params)                  # terminating the worker thread
                return

            output = target(params)             # execute function and place output on queue
            oq.put(output)                      # place output on queue

    def wait(self):
        """
        Start threads and wait for them to finish
        """

        # kick off the output worker which prints output data
        self._threads.append( threading.Thread(target=self._print_output, args=(self._queue_out, self._threads_max)) )
        self._threads[0].start()

        # enque a tag for each thread, signalling it to stop
        for t in range(0, self._threads_max):
            self._queue_in.put(self._queue_tag)

        # kick off the worker threads
        for t in range(1, self._threads_max + 1):
            self._threads.append( threading.Thread(target=self._thread_helper, args=(self._thread_target, self._queue_in, self._queue_out)) )
            self._threads[t].start()

        # wait for threads to finish
        for t in range(0, self._threads_max + 1):
            self._threads[t].join()

    def _print_output(self, oq, max_threads):
        """
        Worker function for output thread
        """
        #global _queue_tag
        t = 0

        while t < max_threads:
            # pop data off the queue
            output = oq.get()

            # check if it is an IWS Queue Tag
            # if so, count and continue
            if output == self._queue_tag:
                t += 1
                continue

            # else print output
            print output

    def log_event(self, **kwargs):

        if "module_id" in self.config:

            item = {
                    "EventType": "2",
                    "ResourceId": self.config["module_id"]
                    }

            if "module_name" in self.config:
                item['ResourceName'] = self.config["module_name"]

            for key in kwargs:
                item[key] = kwargs[key]

            self._api_request_data = {
                "operation": "create",
                "payload": {
                    "Item": item
                }
            }

            self._set_api_request_endpoint(self._log_event_endpoint)
            self._set_api_request_headers()
            api_response = self._call_api()

    def execute_command(self, **kwargs):

        set_json_data = True

        if 'Command' in kwargs:

            command = self._commands[kwargs['Command']]

            if 'Data' in kwargs:
                self._api_request_data = {"Records": kwargs['Data']}
                set_json_data = False

            else:
                item = {}

                for key in kwargs:
                    if key != "Command":
                        item[key] = kwargs[key]

                self._api_request_data = {
                        "operation": command['operation'],
                        "payload": {
                            "Item": item
                        }
                    }

            self._set_api_request_endpoint(command['endpoint'])

            if 'Headers' in kwargs:
                self._api_request_headers = kwargs['Headers']
            else:
                self._set_api_request_headers()

            api_response = self._call_api(set_json_data)

            return api_response

        return False

    def set_tmp_directory(self, **kwargs):

        if 'Path' in kwargs:
            self._tmp_directory = kwargs['Path']
            self._check_directory_exists(self._tmp_directory)

        return True
