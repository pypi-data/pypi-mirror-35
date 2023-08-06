import os
from datetime import datetime
from subprocess import Popen, PIPE
import requests
import shutil
import json

class IWSAgentModule():
    """
    IWS Agent Module

    This is a wrapper class which enabled the seamless transition of modules
    between IWS Console and IWS Agent.

    A module is provided as a self contained ZIP file (which contains the python code)
    and supporting configuration which defines the execution schedule and parameters.

    Scheduling of modules is handled by the IWSAgent using schedule library.
    """

    _config = {}
    _module_id = None
    _module_config = None
    _start_time = None
    finished = False
    _event_output_dir = None
    _event_dir = None
    _logger = None
    _event_id = None

    def __init__(self, config, logger, module_id, module_config=None):
        self._config = config
        self._module_id = module_id
        self._logger = logger

        # allow module config to be passed in (used for events)
        # otherwise try to fetch config from agent config (module instances)
        if module_config == None:
            self.get_module_config()
        else:
            self._module_config = module_config

    def set_module_config(self, cfg):
        self._module_config = cfg

    def set_event_id(self, event_id):
        self._event_id = event_id

    def set_start_time(self):
        # utc = str(datetime.datetime.now()).split('.')[0]
        # utc.replace(' ', '_')
        # utc.replace('')

        self._start_time = str(datetime.utcnow().isoformat('T'))

    def set_utc_datetime(self):
        return str(datetime.utcnow().isoformat('T'))

    def get_module_config(self):
        """
        Using our module ID we can find our specific config

        This is done by traversing the Agent and Device branches
        of the global config to find our module config
        """
        mid = self._module_id
        module_config = None

        for mt in ['Agent', 'Device']:
            cfg = self._config.item(mt)
            if 'ModuleInstances' in cfg:
                for c in cfg['ModuleInstances']:
                    if c['Id'] == mid:
                        module_config = c

        # config found - save for use
        if module_config:
            self._module_config = module_config

    def get_base_dir(self):

        """
        Return the base directory for iws-agent

        This provides us a relative file path to work from
        """
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, os.pardir)

    def get_module_dir(self, module_id):
        """
        Return the module directory for given module_id

        This directory is relative to the base directory of iws-agent
        """
        mdir = os.path.join(self.get_base_dir(), 'modules', module_id)

        if not os.path.isdir(mdir):
            os.mkdir(mdir)

        return mdir

    def get_log_dir(self, module_id):
        """
        Return the log directory for a given module_id

        This directory is relative to the base directory of iws-agent
        """
        log_dir = os.path.join(self.get_base_dir(), 'logs', module_id)

        if not os.path.isdir(log_dir):
            os.mkdir(log_dir)

        return log_dir

    def get_temp_dir(self, event_id):
        """
        Return the tmp directory for a given event_id

        This directory is relative to the base directory of iws-agent
        """
        tmp_dir = os.path.join(self.get_base_dir(), 'tmp')
        event_dir = os.path.join(self.get_base_dir(), 'tmp', event_id)
        self._event_output_dir = os.path.join(event_dir, 'output')


        if not os.path.isdir(tmp_dir):
            os.mkdir(tmp_dir)

        if not os.path.isdir(event_dir):
            os.mkdir(event_dir)

        if not os.path.isdir(self._event_output_dir):
            os.mkdir(self._event_output_dir)

        self._event_dir = event_dir

        return event_dir

    def get_output_filenames(self):
        aid = self._config.item('Agent.Id')
        mid = self._module_id
        start = self._start_time
        log_dir = self.get_log_dir(mid)

        fout = False
        ferr = False

        if self._event_output_dir:

            fout_name = '{}-{}-{}-stdout'.format(aid, mid, start)
            ferr_name = '{}-{}-{}-stderr'.format(aid, mid, start)

            if 'StdOutDestination' in self._module_config:
                if self._module_config['StdOutDestination'] == "events":
                    fout_name = "{{iws-system}}iws_console-" + fout_name
                    ferr_name = "{{iws-system}}iws_console-" + ferr_name

            fout = os.path.join(self._event_output_dir, fout_name)
            ferr = os.path.join(self._event_output_dir, ferr_name)

        else:
            fout = os.path.join(log_dir, fout_name)
            ferr = os.path.join(log_dir, ferr_name)

        return (fout, ferr)

    def save_output(self, stdout, stderr):
        fout, ferr = self.get_output_filenames()

        if fout and len(stdout) > 0:
            with open(fout, 'w') as f:
                f.write(stdout)

        if ferr and len(stderr) > 0:
            with open(ferr, 'w') as f:
                f.write(stderr)


    def upload_file(self, file_object):

        if os.path.exists(file_object):

            fdir, fname = os.path.split(file_object)
            iws_filename = '{}/{}'.format(self._module_config['OutputContainerId'], fname)
            #print(iws_filename)
            result = self._config._client.upload_data(iws_filename)
            #print(result)

            if result['success']:
                url = result['result']['url']

                with open(file_object) as f:
                    #print(f.read())
                    r = requests.put(url, data=f.read(), headers={'Content-Type': 'application/octet-stream'})

                    # success - we can delete local file
                    if r.status_code == requests.codes.ok:
                        os.unlink(file_object)
                    #else:
                        # TODO: log error
                    #    pass


    def upload_output(self):

        #output_continer = self._module_config['OutputContainerId']

        if self._event_output_dir:
            for root, dirs, files in os.walk(self._event_output_dir):
                #print(root)
                if files:
                    for name in files:
                        if "config.json" in name:
                            continue

                        file_object = root + "/" + name
                        self.upload_file(file_object)


                        '''
                        if os.path.exists(file_object):
                            fdir, fname = os.path.split(file_object)
                            iws_filename = '{}/{}'.format(output_continer, fname)
                            #print(iws_filename)
                            result = self._config._client.upload_data(iws_filename)
                            #print(result)

                            if result['success']:
                                url = result['result']['url']
                                with open(file_object) as f:
                                    #print(f.read())
                                    r = requests.put(url, data=f.read(), headers={'Content-Type': 'application/octet-stream'})

                                    # success - we can delete local file
                                    if r.status_code == requests.codes.ok:
                                        os.unlink(file_object)
                                    else:
                                        # TODO: log error
                                        pass
                        '''

    def upload_output_from_module_dir(self, mdir, mdir_old_list):

        #output_continer = self._module_config['OutputContainerId']

        if mdir and mdir_old_list:
            mdir_new_list = os.listdir(mdir)

            for item in mdir_new_list:
                item_path = os.path.join(mdir, item)
                if item in mdir_old_list:
                    if item == "config.json":
                        os.unlink(item_path)
                    continue

                if os.path.isfile(item_path):
                    if item_path[-4:] == '.pyc':
                        continue

                    self.upload_file(item_path)

                elif os.path.isdir(item_path):
                    for root, dirs, files in os.walk(item_path):
                        if files:
                            for name in files:
                                file_object = root + "/" + name
                                self.upload_file(file_object)

                    shutil.rmtree(item_path)

    def parse_arguments(self):

        args = []

        if 'Parameters' not in self._module_config or len(self._module_config['Parameters']) == 0:
            return args

        for a in self._module_config['Parameters']:
            if 'option' in a:
                k = a['option']  # argument
                args.append(k)

            if 'value' in a:
                v = a['value']   # optional value
                if 'TriggerFilename' in self._module_config:
                    v = v.replace('{{input_file}}', self._module_config['TriggerFilename'])

                args.append(v)

        return args

    def run(self):

        self._logger.info("Module Instance {} started at {}".format(self._module_id, self.set_utc_datetime()))
        self._logger.info("Event Directory" + self._event_dir)

        self.set_start_time()

        mid = self._module_id
        cfg = self._module_config
        mdir = self.get_module_dir(mid)
        base_dir = self.get_base_dir()

        # Log EventType Module Instance In Progress
        self._config._client.log_event(cfg['Id'], cfg['ModuleName'], "2", "Event from Agent " + cfg['AgentId'])

        # Download Trigger file, if any
        if 'TriggerFilename' in cfg:
            self._config._client.log_event(cfg['Id'], cfg['ModuleName'], "10", "Downloading Event File, Agent " + cfg['AgentId'])

            trigger_filename = cfg['TriggerFilename']
            temp_file = trigger_filename.split('/')[-1]
            input_file = os.path.join(self._event_dir, temp_file)
            self._config._client.download_data(trigger_filename, input_file)
            cfg['TriggerFilename'] = input_file
            self._module_config['TriggerFilename'] = input_file

        self._logger.info(cfg)

        # Write Config Based on Event received
        #config_file_path = os.path.join(self._event_output_dir, "config.json")
        config_file_path = os.path.join(mdir, "config.json")

        if "AgentKey" in cfg:
            config_data = { 'agent_key' : cfg['AgentKey'] }

            if "InputContainer" in cfg:
                config_data['containers'] = cfg['InputContainer']

            if "OutputContainerId" in cfg:
                config_data['output_container'] = cfg['OutputContainerId']

            if "Id" in cfg:
                config_data['module_id'] = cfg['Id']

            if "TriggerFilename" in cfg:
                config_data['file_object_key'] = cfg['TriggerFilename']

            if "ChartType" in cfg:
                config_data['chart_type'] = cfg['ChartType']

            fh = open(config_file_path,'w')
            fh.write(json.dumps(config_data, indent=4));
            fh.close();

        # construct the command to execute
        filename = cfg['ProgramFilename']

        if "TriggerFilename" in cfg:
            filename = str(cfg['ProgramFilename']).replace("{{input_file}}", str(cfg['TriggerFilename']))

        args = self.parse_arguments()

        #print 'ARGS'
        #print args

        #full_path = os.path.join(mdir, filename)
        full_path = filename

        # Change the Working directory to event output directory before module run
        #if self._event_output_dir:
        #    os.chdir(self._event_output_dir)

        # Change the Working directory to module directory before module run
        mdir_old_list = os.listdir(mdir)
        os.chdir(mdir)

        # if .py we will execute with python in path
        if os.path.isfile(full_path):
            if filename[-3:] == '.py':
                cmd = ['python', full_path]
            else:
                cmd = [full_path]
        else:
            # Since file doesn't exixt in directory, we have binary file
            cmd = [filename]

        # append the arguments if any specified
        # TODO: check how args are passed, may need to parse
        if len(args) > 0:
            cmd = cmd + args

        #print(cmd)
        self._logger.info(cmd)
        p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()

        # Change the Working directory to Base after module run
        os.chdir(base_dir)

        self.save_output(stdout, stderr)

        # Upload Output and Remove event directory
        self.upload_output()

        # Upload if amy output present in module directory
        self.upload_output_from_module_dir(mdir, mdir_old_list)

        # This will remove event dir along with all files, after return from upload_output
        shutil.rmtree(self._event_dir)

        #if 'TriggerFilename' in cfg:
        #    tf = cfg['TriggerFilename']
        #    td = os.path.dirname(tf)

        #    if os.path.isfile(tf):
        #        os.unlink(tf)

            # if os.path.isdir(td):
            #     os.unlink(td)

        # Log EventType Module Instance Complete
        self._config._client.log_event(cfg['Id'], cfg['ModuleName'], "3", "Event from Agent " + cfg['AgentId'], self._event_id)

        self._logger.info("Module Instance Completed {} started at {}".format(self._module_id, self.set_utc_datetime()))

        self.finished = True
