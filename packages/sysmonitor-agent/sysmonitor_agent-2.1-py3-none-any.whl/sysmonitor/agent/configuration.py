"""
Configuration Module

It loads the configuration from a file and loads the default when a missing
configuration is detected
"""
import os
import argparse
import configparser
import logging
import collections

from sysmonitor.agent import utils


_LOGGER = logging.getLogger(__name__)

class Configuration():
    """Configuration Module"""

    @staticmethod
    def _default_config():
        """Default configuration"""
        return {
            "interface": {
                "package": "sysmonitor.agent.interfaces.rest"
            },
            "interface_rest": {
                "bind_address": "127.0.0.1",
                "bind_port": "8068",
                "reload_config_on_request": "False"
            },
            "interface_push": {
                "url": "",
                "method": "put",
                "username": "",
                "password": "",
                "expected_status": "200",
                "interval": 5
            },
            "report": {
                "load_index": 1,
                "systemd": "True",
                "systemd_services": "",
            },
            "authentication": {
                "public": False,
                "key": utils.random_str(),
                "package": "sysmonitor.agent.auth"
            },
            "logging": {
                "file": "/var/log/sysmonitor/agent.log",
                "level": logging.INFO,
                "format": "%%(levelname)s:%%(name)s: %%(message)s"
            }
        }

    @staticmethod
    def _parse_args(parse_cmd, config_file, debug, notify):
        """
        Parse command line arguments (if say so)

        :param bool parse_cmd: If True, it parses command line arguments
        :param string config_file: Configuration file. Used when parse_cmd if False
        :param bool debug: Debug flag. Used when parse_cmd is False
        :param bool notify: Single notification mode. Used when parse_cmd is False
        :return: Named tuple with arguments
        :rtype: tuple
        """
        _LOGGER.debug("Loading arguments")
        if parse_cmd:
            parser = argparse.ArgumentParser(description="System Monitor Agent")
            parser.add_argument("-c", "--config", type=str,
                                help="Configuraton file",
                                default="/etc/sysmonitor/agent.ini")
            parser.add_argument("--debug", action="store_true",
                                help="Debug mode")
            parser.add_argument("-n", "--notify", action="store_true",
                                help="Single push notification")
            return parser.parse_args()
        if not config_file:
            raise AttributeError("Invalid configuration. "
                                 "You must specify the configuration file if "
                                 "not using cmd arguments")
        Config = collections.namedtuple("Configuration",
                                        ["config", "debug", "notify"])
        return Config(config=config_file, debug=debug, notify=notify)

    def _load(self, dolog=False):
        """
        Load configuration from file and default configurations

        :param bool dolog: It logs if True
        """
        if os.path.exists(self._config_file):
            self._config.read(self._config_file)
            for section, settings in self._default_config().items():
                if not self._config.has_section(section):
                    self._config.add_section(section)
                for setting, value in settings.items():
                    if self._config.get(section, setting, fallback=None) is None:
                        self._config.set(section, setting, str(value))
        else:
            self._config.read_dict(self._default_config())
        if self.get("magic", "notify"):
            if dolog:
                _LOGGER.info("--notify (-n) option is set. "
                             "Forcing sysmonitor.agent.interfaces.push as "
                             "interface class.")
            self._config.set("interface", "package",
                             "sysmonitor.agent.interfaces.push")

    def __init__(self, parse_cmd=True, config_file=False,
                 debug=False, notify=False):
        """
        Configuration Module.

        :param bool parse_cmd: If True, it parses command line arguments
        :param string config_file: Configuration file. Used when parse_cmd if False
        :param bool debug: Debug flag. Used when parse_cmd is False
        :param bool notify: Single notification mode. Used when parse_cmd is False
        """
        args = self._parse_args(parse_cmd, config_file, debug, notify)
        self._config_file = args.config
        _LOGGER.debug("Configuration file is %s", self._config_file)

        self._magic = {"debug": args.debug, "notify": args.notify}

        self._config = configparser.SafeConfigParser()
        self._load(dolog=True)


    def reload(self):
        """Reload configuration"""
        _LOGGER.info("Reloading configuration")
        self._load(dolog=False)

    def get(self, section, setting):
        """
        Get a configuration setting

        :param string section: Configuration section
        :param string setting: Required setting to get
        :return: Configuration value
        :rtype: str
        """
        if section not in self._config or setting not in self._config[section]:
            if section == "magic" and setting in self._magic:
                return self._magic[setting]
            raise ValueError("Invalid setting %s on section %s" % (setting,
                                                                   section))
        return self._config.get(section, setting)

    def setlog(self):
        """Set log configuration"""
        debug = self.get("magic", "debug")
        level = logging.DEBUG if debug else self.get("logging", "level")

        logging.basicConfig(level=int(level),
                            filename=self.get("logging", "file") or None,
                            format=self.get("logging", "format"))
        logging.captureWarnings(True)
