"""A REST API service interface"""

import logging
import flask

from sysmonitor.agent import utils, auth
from sysmonitor.agent.interface import BaseInterface
from sysmonitor.agent.configuration import Configuration

_LOGGER = logging.getLogger(__name__)


def authenticate(force_auth):
    """
    Authentication REST API requests

    :param bool force_auth: force_auth parameter passed to the authenticate
                            method from Auth class
    :return: Rest method that handles the request, or Flask abort reponse
    :rtype: function
    """

    def do_auth(fnc):
        def wrapper(*args, **kwargs):
            apikey = flask.request.headers.get("Authorization", None)
            authentication = auth.load(Configuration())
            if not authentication.authenticate(apikey, force_auth=force_auth):
                flask.abort(401)
            return fnc(*args, **kwargs)
        return wrapper
    return do_auth


class Interface(BaseInterface):
    """Create a http server to serve a REST API"""

    def __init__(self, *k, **kw):
        """
        Rest API to serve sysmonitor agent.
        This is the default interface.
        """
        super(Interface, self).__init__(*k, **kw)
        self.flask = flask.Flask(kw.get("appname", "sysmonitor.agent"))

        # Endpoints
        self.flask.add_url_rule("/report", "report", self.rest_report)
        self.flask.add_url_rule("/run/command/", "command",
                                self.rest_run_command, methods=["POST"])
        self.flask.add_url_rule("/run/script/", "script",
                                self.rest_run_script, methods=["POST"])

        # Errors
        self.flask.register_error_handler(500, self.rest_on_error_500)
        self.flask.register_error_handler(401, self.rest_on_error_401)
        self.flask.register_error_handler(405, self.rest_on_error_405)

    def start(self):
        """Run HTTP server"""
        self.flask.run(host=self.config.get("interface_rest", "bind_address"),
                       port=self.config.get("interface_rest", "bind_port"),
                       debug=self.config.get("magic", "debug"))
        return True

    @staticmethod
    def _on_error_json(error):
        """
        Convert exception to JSON format to use with error handlers

        :param Exception error: Exception to parse
        :return: Dictionary with error type and message
        :rtype: dict
        """
        return {
            "error": {
                "type": error.__class__.__name__,
                "message": str(error)
                }
            }

    def rest_on_error_500(self, error):
        """
        Handler for 500 HTTP error

        :param Exception error: Exception to parse
        :return: HTTP JSON response with error
        :rtype: HTTP response
        """
        return flask.jsonify(self._on_error_json(error)), 500

    def rest_on_error_401(self, error):
        """
        Handler for 401 HTTP error

        :param Exception error: Exception to parse
        :return: HTTP JSON response with error
        :rtype: HTTP response
        """
        return flask.jsonify(self._on_error_json(error)), 401

    def rest_on_error_405(self, error):
        """
        Handler for 405 HTTP error

        :param Exception error: Exception to parse
        :return: HTTP JSON response with error
        :rtype: HTTP response
        """
        return flask.jsonify(self._on_error_json(error)), 405

    @authenticate(False)
    def rest_report(self):
        """
        Route to serve machine status

        :param string apikey: API authentication key
        :return: HTTP JSON response with system status
        :rtype: HTTP response
        """
        if utils.str_to_bool(self.config.get("interface_rest",
                                             "reload_config_on_request")):
            self.config.reload()
        return flask.jsonify(self.get_report())

    @authenticate(True)
    def rest_run_command(self):
        """
        Route to execute a command on the host

        :param string apikey: API authentication key
        :return: HTTP JSON response with execution result
        :rtype: HTTP response
        """
        data = flask.request.get_json()
        return flask.jsonify(self.execute_command(data.get("command")))

    @authenticate(True)
    def rest_run_script(self):
        """
        Route to execute a script on the host

        :param string apikey: API authentication key
        :return: HTTP JSON response with execution result
        :rtype: HTTP response
        """
        data = flask.request.get_json()
        if not data or not isinstance(data, dict) or \
                not isinstance(data.get("content", False), str):
            flask.abort(400)
        content = data.get("content")
        executable = data.get("executable", False)
        return flask.jsonify(self.execute_script(content, executable))
