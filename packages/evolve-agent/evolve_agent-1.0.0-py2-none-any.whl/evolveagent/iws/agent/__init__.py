import json
import sys
import os
import platform
import logging
import time
import signal
import socket
from subprocess import Popen, PIPE
import zipfile
import requests
import schedule
import shutil
import uuid
import threading

# TODO: bundle schedule with agent

from evolveagent.iws.agent.config import IWSAgentConfig
from evolveagent.iws.agent.logger import IWSAgentLogger
from evolveagent.iws.agent.module import IWSAgentModule
from evolveagent.iws.caller import IWSClientCaller

from pprint import pprint

AGENT_VERSION = 1.0  # current agent version

###############################################################################
# IWS AGENT
#
# TODO:
# - Add SSL suppoort - http://flask.pocoo.org/snippets/111/
# - Tamper protection - https://github.com/jamercee/signet
# - Insert logging again - refer to original prototype (Beaver)
# - Use a queue of limited size (1000 items) for logging (last X events)
# - Custom JSON encoder which honors OrderedDict
###############################################################################

class IWSAgent():
    _config       = {}    # agent configuration
    _base_dir     = None  # base directory of script
    _modules_path = None  # modules path
    _config_file  = None  # config file
    _log_file     = None  # log file
    _logger       = None  # logger class
    _client       = None  # IWS client
    _modules      = {}    # modules instances
    _update_freq  = None  # update config every N units
    _update_unit  = None  # unit of config update [minutes | hours | days]
    _schedule_module_list = []

    def __init__(self,
                 modules_path='/var/lib/evolve-agent/modules',
                 config_file='/etc/evolve-agent/config.json',
                 log_file='/var/log/evolve-agent.log'):
        """
        IWS Agent Constructor

        This will setup the agent and perform a few sanity checks along the way.
        - Check that the configuration file is present
        - Load the agent config, this is a JSON file
        - Iterate over the list of modules in the modules directory
        - Determine if we are configured as a ProxyAgent, setting up self accordingly
        - Start any background modules as background threads
        """
        self._modules_path = modules_path
        self._config_file = config_file

        # sanity check config file exists
        if not os.path.isfile(self._config_file):
            raise Exception("IWS Agent configuration file '{}' does not exist, exiting".format(self._config_file))

        # instantiate configuration class
        self._config = IWSAgentConfig(self._config_file)

        # instantiate logger and associate with config
        self._logger = IWSAgentLogger('agent', log_file, logging.DEBUG)
        self._config._logger = self._logger

        # load the config
        self._config.load()

        # instantiate two schedules
        # - one to manage the agent config refresh
        # - one other to manage module execution
        self._scheduler_a = schedule.Scheduler()  # agent scheduler
        #self._scheduler_m = schedule.Scheduler()  # module scheduler 2017-11-30 No more schedule of modules as it will rn in cloud and push message

        # grab the IWS URL and Auth token from our config
        #iws_url = self._config.item('IWS.ApiEndpoint')

        # HACK: until IWS Console provides URL this is a fallback
        '''
        if iws_url == None:
            iws_url = "https://1f54ea3ddl.execute-api.us-east-1.amazonaws.com"
            self._config.item('IWS.ApiEndpoint', iws_url)
        '''

        iws_auth = 'Bearer agentkey:{}'.format( self._config.item('Agent.Key') )

        # work out if we need to provide any proxy settings
        proxy = self.get_proxy()

        region = self.get_region()

        # instantiate our IWS Client to interact with IWS Console
        self._client = IWSClientCaller(iws_auth, proxy, region)
        self._client._logger = self._logger

        # attached both the client and config objects to the config object
        # so that it can be leveraged within the config object
        self._config._client = self._client

        # TODO: test file upload then remove
        # f = 'foo/bar/file'
        # r = self._client.upload_data('')
        # sys.exit(1)

        # register device if required
        if not self._config.item('Device.Id'):
            self._logger.info("Device Id not found, registering Agent.")
            self.register_agent()

        # update agent settings based on config
        self.update_config()

        # start the event loop
        self._logger.info("Agent starting scheduler loop")
        while True:
            # schedule.run_pending()
            self._scheduler_a.run_pending()
            #self._scheduler_m.run_pending() 2017-11-30 No more schedule of modules as it will rn in cloud and push message
            self.manage_modules()
            time.sleep(1)

    def manage_modules(self):
        self._logger.debug('CALL manage_modules()')

        # for tid, t in self._modules.iteritems():
        #     # TODO: spawn thread to upload results if present

        #     # thread finished - mark for removal
        #     if not t.isAlive():
        #         t.handled = True

        # remove finished threads from dictionary
        self._modules = {mid: m for mid, m in self._modules.iteritems() if not m.finished }


    def get_proxy(self):
        """
        Return the proxy string from config

        The proxy must be provided as host:port and optionally with
        credentials which are prepended as user:pass@host:port
        """
        proxy = self._config.item('Proxy')

        # no proxy configuration specified
        if proxy == None or proxy == '':
            return None

        # if proxy authentication provided include in config string
        proxy_user = self._config.item('ProxyUser')
        proxy_pass = self._config.item('ProxyPass')

        if proxy_user != None and proxy_pass != None:
            creds = '{}:{}@'.format(proxy_user, proxy_pass)

        return '{}{}'.format(proxy, creds)

    def get_region(self):
        """
        Return the region string from config

        """
        region = self._config.item('region')

        # no region in configuration
        if region == None or region == '':
            return None

        return region

    def start_module(self, module_id, filename, args, output_container):
        """
        Start a module as a background process
        """
        self._logger.debug("SCHEDULED MODULE - START")
        self._logger.debug("SCHEDULED MODULE - ModuleID:  {}".format(module_id))
        self._logger.debug("SCHEDULED MODULE - Filename:  {}".format(filename))
        self._logger.debug("SCHEDULED MODULE - Argyments: {}".format(args))
        self._logger.debug("SCHEDULED MODULE - Container: {}".format(output_container))
        self._logger.debug("SCHEDULED MODULE - END")

        if module_id in self._modules:
            self._logger.info('Module {} appears to already be running, skipping'.format(module_id))
            return

        guid = uuid.uuid4()
        self._modules[module_id] = IWSAgentModule(self._config, self._logger, module_id)
        temp_dir = self._modules[module_id].get_temp_dir(str(guid))
        self._modules[module_id].run()

        # TODO: add exception handling
        # TODO: execute module, pref. async and catch results

        # create log dir if not exists
        # construct filenames for stdout and stderr a-d-m-YYMMDDhis
        # run subprocess in thread

    def start_module_event(self, event_id, module_id, module_config):
        """
        Start an IWS module using an event, as opposed to a schedule which is
        executed using the start_module function
        """

        #print("Before start module event", os.getcwd())
        base_directory = os.getcwd()

        self._logger.debug('CALL start_module_event()')

        #if module_id in self._modules:
        #    self._logger.info('Module {} appears to already be running, skipping'.format(module_id))
        #    return

        self._modules[event_id] = IWSAgentModule(self._config, self._logger, module_id, module_config)

        # Set event Id
        self._modules[event_id].set_event_id(event_id)

        # Set output dir for module event
        module_event_dir = self._modules[event_id].get_temp_dir(event_id)
        module_config['AgentKey'] = self._config.item('Agent.Key')
        module_config['AgentId'] = self._config.item('Agent.Id')

        self._modules[event_id].set_module_config(module_config)

        # Log EventType Module Instance Launch
        self._client.log_event(module_config['Id'], module_config['ModuleName'], "1", "Event from Agent " + self._config.item('Agent.Id'), event_id)

        self._modules[event_id].run()

        # Change working directory to root after module finish job
        #os.chdir(base_directory)
        #print("After module event", os.getcwd())

    def update_agent_schedule(self):
        """
        Update the agent schedule

        The agent schedule is responsible for managing background
        worker threads (thread per module event) and downloading the
        latest configuration definitions from IWS Console
        """

        self._logger.debug('CALL update_agent_schedule()')

        # we need to see if the config frequency and unit
        # varies from the current configuration
        freq = self._config.item('Agent.PollingFrequency')
        unit = self._config.item('Agent.TimeUnit')

        # no change, nothing to do
        if freq == self._update_freq and unit == self._update_unit:
            return

        units = {
            'minutes': lambda f: self._scheduler_a.every(f).minutes.do(self.update_config),
            'hours'  : lambda f: self._scheduler_a.every(f).hours.do(self.update_config),
            'days'   : lambda f: self._scheduler_a.every(f).days.do(self.update_config)
        }

        freq = int(freq)  # ensure represented as integer and not string

        # update the job schedule
        units[unit](freq)

        # save the unit and freq so we can compare
        # when config changes and determine action required
        self._update_freq = freq
        self._update_unit = unit
        self._logger.info('Scheduled config update every {} {}'.format(freq, unit))

        # ensure we don't have multiple jobs in the schedule
        if len(self._scheduler_a.jobs) > 1:
            del self._scheduler_a.jobs[1:]

    def update_config(self):
        """
        Download configuration update from IWS Console

        Additionally, process any changes in configuration, as reflected
        in the newly downloaded configuration
        """
        self._logger.debug('CALL update_config()')
        self._config.download(self._config._client)
        #self.download_all_modules() 2017-11-30 No more download of modules
        self.update_agent_schedule()
        #self.schedule_modules() 2017-11-30 No more schedule of modules as it will rn in cloud and push message

        print "AGENT JOBS"
        print self._scheduler_a.jobs

        #print "MODULE JOBS" 2017-11-30 No more schedule of modules as it will rn in cloud and push message
        #print self._scheduler_m.jobs  2017-11-30 No more schedule of modules as it will rn in cloud and push message

        # add some dynamic variables to config which aren't saved
        self._config.item('Agent.Version', AGENT_VERSION)
        self._config.item('Device.Platform', platform.system())

        # as part of the config refresh we will also poll for messages
        # this may be moved out later so that it can run on a unique schedule
        self.fetch_messages()

        # comment the cleanup for the time being
        #self.cleanup_modules()

    def cleanup_modules(self):
        """
        Cleanup old modules which have reached a certain age
        """
        self._logger.debug('CALL fetch_messages()')
        now = time.time()
        max_age = now - (86400 * 7)

        mdir = self._modules_path

        for path, dirs, files in os.walk(mdir):
            for d in dirs:
                full_path = os.path.join(mdir, d)
                mtime = os.path.getmtime(full_path)
                if mtime < max_age:
                    self._logger.info('Deleting old module - {}'.format(d))
                    shutil.rmtree(full_path)

            ''' I will keep this;but removed cleanup
            if files:
                for name in files:
                    full_path = path + "/" + name
                    mtime = os.path.getmtime(full_path)
                    if mtime < max_age:
                        self._logger.info('Deleting old module - {}'.format(full_path))
                        shutil.rmtree(path)
            '''

        ''' Original From Chris; Failed to traverse directory
        for path, dirs, files in os.walk(mdir):
            for d in dirs:
                full_path = os.path.join(mdir, d)
                mtime = os.path.getmtime(full_path)
                if mtime < max_age:
                    self._logger.info('Deleting old module - {}'.format(d))
                    shutil.rmtree(full_path)
        '''

    def fetch_messages(self):
        """
        Poll messages (event data) which need to be processed by the agent
        """
        self._logger.debug('CALL fetch_messages()')
        device_id = self._config.item('Device.Id')
        messages = self._client.fetch_messages(device_id)

        command_list = []
        if isinstance(messages, list):
            for m in messages:

                module_id = m['Message']['Id']
                module_config = m['Message']

                # download the module if not already present
                self.download_module(m['Message'])

                command_list.append({'event_id': m['EventId'], 'module_id': module_id, 'module_config': module_config})

                # download input data
                # trigger_filename = m['TriggerFilename']
                # self.download_input(event_id, trigger_filename)

                # start module
                #self.start_module_event(event_id, module_id, module_config)

            if len(command_list) > 0:
                threads = [threading.Thread(target=self.start_module_event, args=(command['event_id'],command['module_id'],command['module_config'])) for command in command_list]
                for thread in threads:
                    thread.start()

    def schedule_modules(self):
        """
        Background scheduler for agent modules

        Both Agent and Device module types will be scheduled
        """
        self._logger.debug('CALL start_scheduler()')

        # TODO: find better way to remove duplicates from schedule
        # TODO; option may be to hash config and only update if hash changed

        #del self._scheduler_m.jobs[0:]

        for mt in ['Agent', 'Device']:
            cfg = self._config.item(mt)

            if 'ModuleInstances' in cfg:
                for m in cfg['ModuleInstances']:
                    if m['EventType'] == 'scheduled':
                        self.schedule_module(m)
                        self._logger.info("Scheduled module {}".format(m['Id']))

        # remove duplicate jobs from schedule
        # by converting to a set then back to a list
        # the duplicate entries are removed
        # jobs = set(self._scheduler_m.jobs)
        # self._scheduler_m.jobs = list(jobs)

    def schedule_module(self, mi):
        """
        Schedule a module instance based on it's configuration
        """
        self._logger.debug('CALL schedule_module()')
        interval = mi['Frequency']
        module_id = mi['Id']
        filename = mi['ProgramFilename']
        args = mi['Parameters'] if 'Parameters' in mi else []
        output_container = mi['OutputContainerId']

        for already_schedule in self._schedule_module_list:
            if already_schedule['module_id'] == mi['Id'] and already_schedule['frequency'] == mi['Frequency'] and already_schedule['time_unit'] == mi['TimeUnit']:
                return

        self._schedule_module_list.append({"module_id": mi['Id'], "frequency": mi['Frequency'], "time_unit": mi['TimeUnit']})

        if mi['TimeUnit'] == 'minutes':
            self._scheduler_m.every(interval).minutes.do(self.start_module, module_id, filename, args, output_container)
        elif mi['TimeUnit'] == 'hours':
            self._scheduler_m.every(interval).hours.do(self.start_module, module_id, filename, args, output_container)
        elif mi['TimeUnit'] == 'days':
            self._scheduler_m.every(interval).days.do(self.start_module, module_id, filename, args, output_container)

    def register_agent(self):
        """
        IWS Agent Registration

        This process will call the IWS Console and register the specific "device",
        a device is an instance of a particular Agent

        During registration an Device ID will be generated and returned,
        this ID is stored within the config and written to disk
        """
        self._logger.debug('CALL register_agent()')

        data = {
            "Name": socket.gethostname(),
            "AgentId": self._config.item('Agent.Id')
        }

        res = self._client.register_agent_device(data)

        if res['success']:
            device_id = res['result']['DeviceId']
            self._config.item('Device.Id', device_id)
            self._config.save()
            self._logger.debug("Device registration successful, new Device ID: {}".format(device_id))
        else:
            # TODO: exit agent and log error
            self._logger.debug("Device registration failed")
            sys.exit(1)

    def start(self):
        """
        Start the Agent

        This will start the RESTful API (Flask) and setup each of the REST routes.

        We default to listening on all addresses (might change to config option) and
        listen on a port defined within the agent config (default: 4321).

        Additionally the Flask server is configured to run as threaded, this allows it
        to answer more than one request at a time, required for features such as ProxyAgent
        which would otherise cause a deadlock. :(
        """

        self._logger.debug('CALL start()')
        self._logger.info("IWS agent starting")

        # first we need to see if registration is required
        if not self._config.item('Device.Id'):
            self.register_agent()

        # self._config.download()  # download latest config from IWS Console
        self.update_config()     # update agent settings based on config

        # start RESTful API
        # self.start_rest_api()

        # start backgorund MODULES
        #self.start_background_modules()

        self._logger.info("Agent starting scheduler loop")
        while True:
            # schedule.run_pending()
            self._scheduler_a.run_pending()
            #self._scheduler_m.run_pending()
            time.sleep(1)

    def stop(self):
        """
        Gracefully stop the IWS Agent.

        This process should stop each of the background modules which run in threads.
        """
        self._logger.debug('CALL stop()')

        pid = os.getppid()  # parent PID (as called from Flask)
        # pgid = os.getpgid(pid)
        os.kill(pid, signal.SIGINT)
        #exit(0)

    def get_module_dir(self, module_id):
        """
        Return the directory where a module should be downloaded

        By default this should be a module subdirectory under the
        relative /modules directory within the Agent installation
        """
        self._logger.debug('CALL get_module_dir()')

        mdir = self._modules_path
        if not os.path.isdir(mdir):
            os.mkdir(mdir)

        return os.path.join(self._modules_path, module_id)

    def download_all_modules(self):
        """
        Download all IWS Modules

        This is a wrapper around the download_module function
        """
        self._logger.debug('CALL download_all_modules()')

        dm = self._config.item('Device.ModuleInstances')
        am = self._config.item('Agent.ModuleInstances')

        if dm:
            for m in dm:
                self._logger.info("Downloading device module {}".format(m['Id']))
                self.download_module(m)

        if am:
            for m in am:
                self._logger.info("Downloading agent module {}".format(m['Id']))
                self.download_module(m)

    def download_module(self, module_config):
        """
        Download an IWS Module from IWS Console

        A module is provided as a ZIP file which contains related python code.

        We download a module as a 2-step process
        - first we obtain a signed URL using authenticated request
        - second we download the module using signed URL
        """

        self._logger.debug('CALL download_module()')

        # get the directory for the selected module
        mdir = self.get_module_dir(module_config['Id'])

        # check if the modules exists
        # no need to download if already exists
        # simply update mtime so we can cleanup later
        if os.path.isdir(mdir):
            os.utime(mdir, None)
            return

        # Log EventType Module Instance Download in Progress
        self._client.log_event(module_config['Id'], module_config['ModuleName'], "10", "Event from Agent " + self._config.item('Agent.Id'))

        if 'Packages' in module_config:
            packages_array = module_config['Packages'].split("\n")
            run_command = "apt-get update && "
            for package in packages_array[:-1]:
                run_command = run_command + package + " && "

            run_command = run_command + packages_array[-1]

            self._logger.debug('Build Commands - Module {}'.format(run_command))

            popen = Popen(run_command, stdout=PIPE, shell=True)
            popen.communicate()[0]

        self._logger.debug('Download - Module {}'.format(module_config['Id']))

        # request a signed URL from the IWS Console API
        res = self._client.download_module(module_config['Id'])

        # if the download was successful
        if res['status'] == 'ok' and 'url' in res['result']:
            # create the sub-directory for the download
            #os.mkdir(mdir, 0766)  # only allow owner to modify
            os.mkdir(mdir)

            url = res['result']['url']    # signed URL
            zf = '{}/m.zip'.format(mdir)  # zip file destination

            # now we can download the signed URL
            r = requests.get(url, stream=True)
            with open(zf, 'wb') as f:
                for chunk in r.iter_content(2048):
                    f.write(chunk)

            # unzip the module zip into the module directory
            z = zipfile.ZipFile(zf, 'r')
            z.extractall(mdir)
            z.close()

            # remove files not required from list
            remove_filelist = ["iwsclient.py", "caller.py", "docker_caller.py", "context.py"]
            for rfile in remove_filelist:
                rfile_path = mdir + "/" + rfile
                if os.path.isfile(rfile_path):
                    os.unlink(rfile_path)

            #create sym link to iwsclient
            os.symlink(os.path.join(self._base_dir, "iws", 'iwsclient.py'), os.path.join(mdir, 'iwsclient.py'))

            # adding exec permissions to dir to run shell script other than binary
            make_exec_command = "chmod -R +x " + mdir
            exec_result = os.system(make_exec_command)

            # and cleanup the temporary zip file
            os.unlink(zf)

            # Log EventType Module Instance Download in Progress
            self._client.log_event(module_config['Id'], module_config['ModuleName'], "11", "Event from Agent " + self._config.item('Agent.Id'))

        # did not get expected result with a HTTP success
        else:
            # TODO: handle error
            pass
