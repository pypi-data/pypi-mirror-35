"""
Authentication module

This file contains the base authentication mechanism for the agent, but it
can be extended to provide adicional authentication methods.
"""

import logging
from importlib import import_module
from sysmonitor.agent import configuration, utils


_LOGGER = logging.getLogger(__name__)


def load(config=False):
    """
    Loads the authentication module specified on the configuration file

    :param string config: Configuration object
    :return: Authentication module
    :rtype: Auth
    """
    if not config:
        config = configuration.Configuration()
    try:
        auth_class = import_module(config.get("authentication", "package"))
        auth_class = auth_class.Auth
    except Exception as err:
        raise RuntimeError("Unable to import auth class %s" % err)
    return auth_class(config)



class Auth():
    """
    Basic authentication module.

    It checks the API key matches with the one on the configuration file.
    If only checks for a valid authentication if the authentication isn't
    public or the authentication is required.
    """

    def __init__(self, config):
        """
        Basic authentication module

        :param Configuration config: Configuration object
        """
        self.config = config

    def is_public(self):
        """Check if authentication is disable"""
        return utils.str_to_bool(self.config.get("authentication",
                                                 "public"))

    def authenticate(self, apikey=False, force_auth=False):
        """
        Authenticate method. Use it to check if the authentication key is valid

        :param string apikey: API key to check
        :param bool force_auth: If True, will ignore public authentication
        :return: True if valid authentication
        :rtype: Bool
        """
        syskey = self.config.get("authentication", "key")
        if (force_auth or not self.is_public()) and syskey != apikey:
            _LOGGER.error("Invalid authentication token")
            return False
        return True
