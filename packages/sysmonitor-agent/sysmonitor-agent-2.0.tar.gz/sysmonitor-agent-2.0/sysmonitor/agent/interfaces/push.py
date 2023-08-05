"""Notification Interface"""

import time
import logging
import requests
from sysmonitor.agent.interface import BaseInterface

_LOGGER = logging.getLogger(__name__)


class Interface(BaseInterface):
    """Send status to a target system via HTTP request"""

    def start(self):
        """
        Send push notifications every x seconds.

        If notify configuration is True, it send only one notification
        """
        if self.config.get("magic", "notify"):
            self.push()
            return True
        interval = int(self.config.get("interface_push", "interval"))
        while True:
            self.push()
            time.sleep(interval)
        return True

    def push(self):
        """Send report to external service via HTTP"""
        url = self.config.get("interface_push", "url")
        username = self.config.get("interface_push", "username")
        password = self.config.get("interface_push", "password")

        auth = (username, password) if username and password else None
        expected_status = self.config.get("interface_push", "expected_status")
        expected_status = [int(x) for x in expected_status.split(",")]
        if not url:
            raise Exception("Notification URL not defined")
        method = getattr(requests, self.config.get("interface_push", "method"))
        _LOGGER.info("Sending notification to %s", url)
        try:
            res = method(url, json=self.get_report(), auth=auth)
            assert res.status_code in expected_status
        except AssertionError:
            raise Exception("Invalid response from notification target")
        return True

    def execute_command(self, command):
        """Push interface doesn't allow command execution"""
        raise NotImplementedError("Push interface doesn't allow "
                                  "command execution")

    def execute_script(self, content, executable=False):
        """Push interface doesn't allow script execution"""
        raise NotImplementedError("Push interface doesn't allow "
                                  "script execution")
