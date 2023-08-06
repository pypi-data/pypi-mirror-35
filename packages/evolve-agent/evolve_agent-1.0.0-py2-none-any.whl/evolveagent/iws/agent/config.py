import json
import os
import requests

class IWSAgentConfig():
    """
    IWS Agent Configuration Manager

    This is a helper class to get, set and download then agent configuration
    from IWS Console using provided APIs.

    By abstracting this class we can pass it between other classes.
    """

    _config      = {}      # dictionary of config
    _config_file = None    # configuration file (JSON)
    _client      = None    # IWS Client
    _logger      = None    # logger object


    def __init__(self, config_file):
        self._config_file = config_file

    def item(self, key=None, value=None):
        """
        Allow retrieval of config values using dot notation to traverse the JSON tree.

        Example JSON configuration:
            { "HttpProxy": { "Server": "proxy.corp.network", "Port": 8080 } }

        Could be accessed as follows:
            get_config('HttpProxy.Server')
            get_config('HttpProxy.Port')

        This function is simply a helper to improve code readability.
        """

        self._logger.debug('CALL IWSAgentConfig.item()')

        # return the entire configuration
        if key is None:
            return self._config

        # get or set a specific value
        else:
            segments = key.split('.')  # split by .
            last = segments[-1]        # keep track of last segment so we can return
            selected = self._config    # keep track of current segment as we walk the config

            # return a specific value
            if value is None:
                for s in segments:
                    if s in selected:
                        selected = selected[s]  # select config node
                        if s == last:           # return if we are at the last segment
                            return selected
                    else:
                        return None  # value not found

            # set a value
            else:
                for s in segments:
                    if s == last:
                        selected[s] = value  # set value
                    if s not in selected:    # check config branch exists
                        selected[s] = {}     # create config branch
                    selected = selected[s]   # select config branch

    def load(self):
        """
        Load the IWS Agent configuration file.

        This is a JSON file which contains pertinant information such as:
        - AgentID       UUID which identifies the agent in IWS
        - ClientID      UUID which identifies the client in IWS
        - ProxyAgent    Configuration flag to signify proxy agent functionality
        - HttpProxy     Ability to utilise a HTTP proxy

        Other configuration options are available this is just some of the basics.

        The configuration file should be retrieved from IWS and an admin is able to
        launch the agent for the first time and specify the ClientID and optionally
        AgentID to download a configuration.
        """
        self._logger.debug('CALL IWSAgentConfig.load()')

        cf = self._config_file

        self._logger.info("Loading configuration")

        if os.path.isfile(cf):                   # sanity check file exists
            try:
                with open(cf, 'r') as f:
                    try:
                        self._config = json.loads(f.read())
                    except ValueError as e:
                        return Exception("Unable to parse IWS Agent config, malformed JSON.")
            except IOError:
                return Exception("Could not read IWS Nessus config.")
        else:
            return Exception("IWS Agent config does not exist '{}'.".format(self.config_file))

    def save(self):
        """
        Save the configuration

        The configuration is saved as pretty JSON to config.json
        """
        self._logger.debug('CALL IWSAgentConfig.save()')

        with open(self._config_file, 'w') as f:
            j = json.dumps(self._config, sort_keys=True, indent=4)
            f.write(j)

    def download(self, callerObject):
        """
        Download agent configuration from IWS Console
        """

        self._logger.debug('CALL IWSAgentConfig.download()')
        self._logger.info('Downloading config from IWS Console')

        #base_url = self.item('IWS.ApiEndpoint')
        #url = '{}/agent/device/updateconfig'.format(base_url)

        agent_id = self.item('Agent.Id')
        agent_key = self.item('Agent.Key')
        device_id = self.item('Device.Id')

        # work out the last time the config was udpated
        agent_date = self.item('Agent.UpdatedDate')
        agent_updated = "" if agent_date == None else agent_date

        device_date = self.item('Device.UpdatedDate')
        device_updated = "" if device_date == None else device_date

        # HACK: override device and agent updated to force module download
        device_updated = ''
        agent_updated = ''

        # payload for the device registration API
        # we provide the agent ID and hostname as the agent name
        '''
        data = {
            "Records": [{
                "operation": "updateconfig",
                "payload": {
			        "Item": {
                        "AgentId": agent_id,
                        "DeviceId": device_id,
                        "AgentUpdatedDate": agent_updated,
                        "DeviceUpdatedDate": device_updated
			        }
		        }
            }]
        }

        headers = {
            "Authorization": "Bearer AgentKey:{}".format(agent_key),
            "Content-Type": "application/json"
        }

        r = requests.post(url, json=data, headers=headers)
        '''

        res = callerObject.update_config(agent_id, device_id, agent_updated, device_updated)

        if 'status_code' in res and res['status_code'] == 200:
            #res = r.json()

            if 'result' in res and 'updated' in res['result']:
                updated = res['result']['updated']

                if updated in ['Both', 'Agent']:
                    self._config['Agent'] = res['result']['config']['Agent']

                if updated in ['Both', 'Device']:
                    self._config['Device'] = res['result']['config']['Device']

                self.save()
        else:
            # TODO: exit agent and log error
            pass



