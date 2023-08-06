# Evolve Agent

Evolve Agent is a daemon to connect your systems to the Evolve Security Automation and Orchestration Platform.

## Content

1. System Requirements
2. Installation
3. Upgrade
4. Uninstall
5. File Locations
6. Evole Agent CLI


## 1. System Requirements

+ Hardware
	- Memory: Mininum 50 MB
	- Disk: Minimum 50 MB
+ Software
	- Operating System: Linux
	- Python: Python 2.7 series, version 2.7.12 and above
	- Init subsystem: systemd, upstart and systemv

## 2. Installation

### Package Installation

Install the evolve-agent using the following command, on Linux:

```bash
sudo pip install evolve-agent
```

### Agent Configuration

Configure the evolve-agent using either of the following commands. To do the configuration interactively:

```bash
sudo evolve-agent --configure --interactive
```

Then, provide the Agent with your configuration details.

```
Enter Agent Polling Unit (minutes, hours, days, weeks): minutes
Enter Agent Polling Frequency: 1
Enter Agent ID: <agent-id>
Enter Agent Key: <agent-key>
Enter Proxy Server: <proxy-host>:<proxy-port>
Proxy Username: <proxy-user>
Proxy Password: <proxy-password>
```

Alternatively, all parameters can be passed on the command-line:

```bash
sudo evolve-agent --configure \
                  --agent-id <agent-id> \
                  --agent-key <agent-key> \
                  --polling-frequency 1 \
                  --polling-unit minutes
```

### Service Installation

```bash
sudo evolve-agent --install
```

#### Service Usage

For systemd:

```bash
sudo systemctl start|stop|restart|status evolve-agent
```

For upstart:

```bash
sudo start|stop|restart|status evolve-agent
```

For systemv (sysvinit):

```bash
sudo /etc/init.d/evolve-agent start|stop|restart|status
```

## 3. Upgrade

### Package Upgrading

```bash
sudo pip install --upgrade evolve-agent
```

### Service Restart

For systemd:

```bash
sudo systemctl restart evolve-agent
```

For upstart:

```bash
sudo restart evolve-agent
```

For systemv (sysvinit):

```bash
sudo /etc/init.d/evolve-agent restart
```

## 4. Uninstall

### Service Uninstalling

```bash
sudo evolve-agent --uninstall
```

### Package Uninstalling

```bash
sudo pip uninstall evolve-agent
```

## 5. File Locations

### Program/Executable

The evolve-agent program can be found in `/usr/local/bin/evolve-agent` or `/usr/bin/evolve-agent`.

### Source Package

The source package can be found in the platform's shared dist-packages directory, commonly in: `/usr/local/lib/python2.7/dist-packages/evolveagent`

### Configuration

The configuration command will generate the config in: `/etc/evolve-agent/config.json`

### Log

The log file can be found at: `/var/log/evolve-agent.log`

## 6. Evole Agent CLI

The Evolve Agent CLI can provide help from the command line.

```
evolve-agent --help
```

Example output from the evolve-agent help:

```
usage: evolve-agent [-h] [-d] [-p PIDFILE] [--install] [--uninstall]
                    [--configure] [--interactive] [--agent-id AGENT_ID]
                    [--agent-key AGENT_KEY]
                    [--polling-frequency POLLING_FREQUENCY]
                    [--polling-unit {minutes,hours,days,weeks}]
                    [--proxy-server PROXY_SERVER]
                    [--proxy-username PROXY_USERNAME]
                    [--proxy-password PROXY_PASSWORD]

Intelligence Web Services Endpoint Agent

optional arguments:
  -h, --help            show this help message and exit
  -d, --daemon          Start Evolve Agent as Daemon
  -p PIDFILE, --pidfile PIDFILE
                        Path of pidfile for Evolve Agent Daemon (require
                        -d/--daemon)
  --install             Install Evolve Agent service
  --uninstall           Install Evolve Agent service
  --configure           Configure Evolve Agent
  --interactive         Configure Evolve Agent interactively (require
                        --configure)
  --agent-id AGENT_ID   Agent ID (require --configure)
  --agent-key AGENT_KEY
                        Agent Key (require --configure)
  --polling-frequency POLLING_FREQUENCY
                        Configure polling frequency [Default: 5] (require
                        --configure)
  --polling-unit {minutes,hours,days,weeks}
                        Polling unit [Default: minutes] (require --configure)
  --proxy-server PROXY_SERVER
                        Proxy server (require --configure)
  --proxy-username PROXY_USERNAME
                        Proxy username (require --configure)
  --proxy-password PROXY_PASSWORD
                        Proxy password (require --configure)
```


