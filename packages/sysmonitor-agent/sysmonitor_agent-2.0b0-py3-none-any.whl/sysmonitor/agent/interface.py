"""
Interface meta class. Extend this class to add custom interfaces
"""

import importlib
import subprocess
import os
import stat
import multiprocessing
import logging
import tempfile
import psutil

try:
    import dbus
except ImportError:
    dbus = False

from sysmonitor.agent import utils
from sysmonitor.agent.configuration import Configuration


_LOGGER = logging.getLogger(__name__)


class BaseInterface():
    """
    Interface meta class

    Extend this class to add new type of interfaces
    """

    def __init__(self, config=False):
        """Interface meta class

        :param sysmonitor.agent.Configuration config: Configuration
        """
        if not config:
            config = Configuration()
        self.config = config

    @staticmethod
    def load(cfg=False):
        """
        Load interface from configuration


        :param sysmonitor.agent.Configuration cfg: Configuration
        :return: Selected interface
        :rtype: sysmonitor.agent.BaseInterface
        """
        if not cfg:
            cfg = Configuration()

        try:
            interface = importlib.import_module(cfg.get("interface",
                                                        "package")).Interface
        except Exception as err:
            raise RuntimeError("Unable to import report class %s" % err)
        return interface(cfg)

    @staticmethod
    def _service_status(service):
        """
        Get a status of a service

        :param string service: service name
        :return: service status
        :rtype: string
        """
        bus = dbus.SystemBus()
        systemd = bus.get_object("org.freedesktop.systemd1",
                                 "/org/freedesktop/systemd1")
        manager = dbus.Interface(systemd,
                                 dbus_interface="org.freedesktop.systemd1.Manager")
        try:
            unit = manager.LoadUnit(service)
        except dbus.exceptions.DBusException:
            return "invalid"
        proxy = bus.get_object("org.freedesktop.systemd1", str(unit))
        state = proxy.Get("org.freedesktop.systemd1.Unit",
                          "ActiveState",
                          dbus_interface="org.freedesktop.DBus.Properties")
        return state

    def get_service_status(self):
        """
        Get status from services

        It returns a dictionary with the services and their state.
        It returns a empty dict if systemd is disabled or dbus isn't installed

        :return: Dictionary with the key services that contains a dictionary
                 with the services (keys) and their status (values)
        :rtype: dict
        """
        check_systemd = utils.str_to_bool(self.config.get("report", "systemd"))
        if not check_systemd:
            return {"services": {}}
        if not dbus:
            _LOGGER.warning("Unable to import dbus. Systemd is disable")
            return {"services": {}}
        result = {}
        services = self.config.get("report", "systemd_services")
        for service in utils.str_to_list(services):
            result[service] = self._service_status(service)

        return {"services": result}

    @staticmethod
    def _system_load(load_index=1):
        """
        Get current system load

        :param int load_index: Index from os.getloadavg() result
        :return: system load in percentage
        :rtype: float
        """
        load_avg = os.getloadavg()[load_index]

        return round(load_avg / multiprocessing.cpu_count() * 100, 2)

    @staticmethod
    def _system_memory():
        """
        Get current system used RAM and SWAP

        :return: tuple with used ram percentage and used swap percentage
        :rtype: tuple
        """
        ram = psutil.virtual_memory()
        swap = psutil.swap_memory()
        ram_perc = round(ram.used / ram.total * 100, 2)
        if swap.total > 0:
            swap_perc = round(swap.used / swap.total * 100, 2)
        else:
            swap_perc = 0

        return ram_perc, swap_perc

    @staticmethod
    def _system_disk():
        """
        Get current usage of system partitions

        :return: Dictionary with mointpoints as keys and usage as values
        :rtype: dict
        """
        res = {}
        for drive in psutil.disk_partitions():
            res[drive.mountpoint] = psutil.disk_usage(drive.mountpoint).percent
        return res

    def get_system_status(self):
        """
        Get current system status: Load (CPU), disk, RAM and SWAP

        :return: Dictionary with the key resources that contains a dictionary
                 with the system status
        :rtype: dict
        """

        ram_perc, swap_perc = self._system_memory()

        result = {"memory": ram_perc, "swap": swap_perc,
                  "disk": self._system_disk(),
                  "load": self._system_load(int(self.config.get("report",
                                                                "load_index")))}

        return {"resources": result}

    def get_system_info(self):
        """
        Get current system info

        * Hostname
        * OS (result of uname)

        :return: Dictionary with system information
        :rtype: dict
        """
        uname = os.uname()
        return {"hostname": uname.nodename, "os": ' '.join(uname)}

    def get_report(self):
        """
        Get report to send. The report is composed by the results of:

        * get_system_info
        * get_system_status
        * get_service_status

        :return: Dictionary with all reports
        :rtype: dict
        """
        return utils.merge_dicts(self.get_system_info(),
                                 self.get_system_status(),
                                 self.get_service_status())

    def start(self):
        """Start interface"""
        raise NotImplementedError("Interface meta class can't be started.")

    def execute_command(self, command):
        """
        Execute a command on the system

        :param string command: Command to be executed
        :return: Dictionary with command return code, stdout and stderr
        :rtype: dict
        """
        if isinstance(command, str):
            command = command.split(" ")
        result = subprocess.run(command)
        _LOGGER.info("Executed command %s (status code: %d)",
                     ' '.join(command), result.returncode)
        return {
            "code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr
        }

    def execute_script(self, content, executable=False):
        """
        Execute commands inside a script

        It writes the script inside a temporary file and execute it.

        If executable is False (default), it gives executation permissions to
        the script file.

        :param string content: Script content
        :param strip executable: Optional executable that runs the script
        :return: Dictionary with return code, stdout and stderr
        :rtype: dict

        """
        script_name = utils.random_str()
        script_path = os.path.join("/", tempfile.gettempdir(), script_name)
        with open(script_path, "w") as script:
            script.write(content)
        if not executable:
            os.chmod(script_path, stat.S_IRWXU)
            command = [script_path]
        else:
            command = ["/usr/bin/env", executable, script_path]
        res = self.execute_command(command)
        os.unlink(script_path)
        return res
