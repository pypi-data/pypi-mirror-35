import requests
import json
from evolveagent.iws.iwsclient import IWSClient


class IWSClientCaller():
    """
    IWS Client Wrapper

    Client to interact with IWS API in a consistent manner.
    """

    _url    = None  # API Endpoint URL
    _auth   = None  # Authorization Header
    _logger = None  # Logger object
    _proxy  = {}    # HTTP Proxy
    _iwsclient = None

    def __init__(self, auth, proxy, region):
        #self._url = url
        self._auth = auth
        self._iwsclient = IWSClient()

        if region != None:
            self._iwsclient.config['region'] = region

        if proxy != None:
            # strip http:// or https:// prefix
            proxy = proxy[7:] if proxy[:7] == 'http://' else proxy
            proxy = proxy[8:] if proxy[:8] == 'https://' else proxy

            self._proxy = {
                'http': 'http://' + proxy,
                'https': 'https://' + proxy,
            }

    '''
    def url(self, url):
        if url[0] == '/':
            print("If am in url {}{}".format(self._url, url))
            return '{}{}'.format(self._url, url)

        print("Outside If, I am in url {}{}".format(self._url, url))
        return '{}/{}'.format(self._url, url)
    '''

    def headers(self):
        """
        Return the standard headers used for each API call.

        This includes our authorization header (Bearer Token) and
        we content type, which defaults to JSON.
        """
        return {
            "Authorization": self._auth,
            "Content-Type": "application/json"
        }

    def data(self, operation, payload):
        """
        Return a standardised data payload (POST data) for each API call.
        """
        return [{ "operation": operation, "payload": { "Item": payload }}]

    def post(self, command, operation, data):
        """
        Submit a POST request to IWS Console API
        """
        headers = self.headers()           # Headers with auth token
        data = self.data(operation, data)  # POST Body

        try:
            '''
            r = requests.post(url, json=data, headers=headers)
            '''

            kwargs = { "Command": command, "Headers": headers}
            kwargs['Data'] = data

            r = self._iwsclient.execute_command(**kwargs)
            j = r.json() # we should always receive a JSON response
            result = j['result'] if 'result' in j else j

            #print(r.status_code)

            #return { 'status_code': r.status_code, 'status': 'ok', 'success': True, 'result': result }

            if r.status_code == 200:
                return { 'status_code': r.status_code, 'status': 'ok', 'success': True, 'result': result }

            return { 'status_code': r.status_code, 'status': 'failed', 'success': False, 'result': j }

        except Exception:
            # requests.exceptions.ConnectionError
            status_code = 0
            if 'r' in locals():
                status_code = r.status_code
            return { 'status_code': status_code, 'status': 'failed', 'success': False, 'result': {} }

    def register_agent_device(self, data):
        """
        Register the device with IWS to obtain a device ID
        """
        return self.post('agent-device-register', 'register', data)

    def download_module(self, module_id):
        """
        Download a module from IWS by ID

        This function returns a signed URL within result['url']
        which enables the module to be downloaded from IWS
        """
        data = { "ModuleInstanceId": module_id }
        return self.post('agent-device-downloadmodule', 'downloadmodule', data)

    def update_config(self, agent_id, device_id, agent_updated, device_updated):
        """
        Download a module from IWS by ID

        This function returns a signed URL within result['url']
        which enables the module to be downloaded from IWS
        """
        data = { "AgentId": agent_id, "DeviceId": device_id, "AgentUpdatedDate": agent_updated, "DeviceUpdatedDate": device_updated }
        return self.post('agent-device-updateconfig', 'updateconfig', data)

    def download_data(self, src, dst):
        """
        Download a file from IWS
        """
        # first fetch a signed URL
        data = { 'FileObjectKey': src }
        result = self.post('agent-device-downloaddata', 'downloaddata', data)

        if result['success']:
            url = result['result']['url']

            r = requests.get(url, stream=True)
            with open(dst, 'wb') as f:
                for chunk in r.iter_content(2048):
                    f.write(chunk)
            return dst
        else:
            return None

    def upload_data(self, filename, content_type='application/octet-stream'):
        """
        Upload content to IWS

        This requires a 2-step process:
        - first a signed URL is requested
        - second the upload occurs using the signed URL
        """
        # request a signed URL
        data = { 'FileObjectKey': filename, 'ContentType': content_type }
        return self.post('agent-device-uploaddata', 'uploaddata', data)

    def fetch_messages(self, device_id):
        """
        Fetch a list of messages which are sitting in our queue

        These messages are generated as part of IWS workflows and are
        used to signal an agent to perform a task (i.e. run a module)
        whilst providing event information, such as the input file.

        Each message will provide (modelled after agent config):
        - Id                 Module Instance id
        - InputContainer     List of input containers
        - ModuleCodeS3Key    S3 Key to download module
        - ModuleName         Cosmetic name for module (purely for logging)
        - OutputContainerId  S3 container for data uploads
        - Parameters         List of paramters for execution
        - ProgramFilename    Executable within module
        - TriggerContainer   S3 container for input trigger
        - TriggerFilename    File within S3 which triggered invocation

        #TODO: currently a stubbed API, need to built API within IWS using with SQS
        """
        data = { 'DeviceId': device_id }
        msg = self.post('agent-device-messages', 'messages', data)
        # print 'MESSAGES RECEIVED'
        # print msg
        return msg['result']

    def log_event(self, resource_id, resource_name, event_type, message=False, reference_id=False):
        """
        Log Event

        Each Event will provide:
        - ResourceId         Module Instance id
        - ResourceName       Cosmetic name for module (purely for logging)
        - EventType          Event Type [0:Error, 1:Instance_Launch, 2:Instance_In_Progress, 3:Instance_Complete ]
        """
        if resource_id and resource_name and event_type:
            data = { 'ResourceId': resource_id, 'ResourceName': resource_name, 'EventType': event_type}

            if message:
                data['Message'] = message

            if reference_id:
                data['ReferenceId'] = reference_id


            return self.post('agent-device-logevent', 'log_event', data)

        return
