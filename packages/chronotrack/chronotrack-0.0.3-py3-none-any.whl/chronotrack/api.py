import logging
import hashlib
import json

import requests

from . import exceptions
from .utils import init_logger


AUTH_OAUTH2_WEB_FLOW = 0
AUTH_OAUTH2_PASSWORD_FLOW = 1
AUTH_HTTP_BASIC_AUTH = 2
AUTH_SIMPLE = 3

API_ENDPOINTS = {
    "production": "https://api.chronotrack.com/api",
    "test": "https://qa-api.chronotrack.com/api"
}


class Chronotrack:
    def __init__(self, client_id, user_id, user_pass, debug=True, log_filepath='ct_api'):
        self.client_id = client_id
        self.user_id = user_id
        self.user_pass = user_pass
        self.user_pass_sha1 = hashlib.sha1(self.user_pass.encode('ascii')).hexdigest()
        self.auth_type = AUTH_SIMPLE
        self.set_debug(debug)
        self.endpoint = API_ENDPOINTS["test"]
        self.log_filepath = log_filepath
        init_logger(log_filepath)

    def set_auth_type(self, auth_type):
        self.auth_type = auth_type

    def set_debug(self, debug=True):
        self.debug = debug
        if self.debug:
            self.endpoint = API_ENDPOINTS["test"]
        else:
            self.endpoint = API_ENDPOINTS["production"]

    def request(self, resource_name, resource_id=None, sub_resource_name=None, *args, format="json", method="GET", **kwargs):
        url = self.endpoint

        # authentication params
        url_params = "client_id={}&user_id={}&user_pass={}".format(self.client_id, self.user_id, self.user_pass_sha1)

        url += "/{}.{}".format(resource_name, format)

        if resource_id:
            url += "/{}".format(resource_id)

        if sub_resource_name:
            url += "/{}".format(sub_resource_name)

        url += "?{}".format(url_params)

        params = "&".join(["{}={}".format(k, v) for k, v in kwargs.items()])
        if params:
            url += "&" + params

        r = requests.request(method=method, url=url)
        if r.ok:
            return json.loads(r.content.decode('utf8'))

    ######################################################
    # APIs

    # Events
    def events(self):
        result = self.request("event")

        return result.get("event", [])

    def event(self, event_id):
        result = self.request("event", resource_id=event_id)

        return result.get("event", {})

    # Races
    def races(self, event_id):
        result = self.request("event", event_id, "race")

        return result.get("event_race", [])

    def race(self, race_id):
        result = self.request("race", race_id)

        return result.get("event_race", {})

    # Entries
    def entries(self, event_id=None, race_id=None, group_id=None):
        args = [event_id, race_id, group_id]
        if args.count(None) != 2:
            exceptions.InvalidCallError("Only one of {} {} {} must present".format('event_id', 'race_id', 'group_id'))

        result = {}
        if event_id:
            result = self.request("event", event_id, "entry")

            return result["event_entry"]
        elif race_id:
            result = self.request("race", race_id, "entry")

            return result["race_entry"]
        elif group_id:
            result = self.request("groups", group_id, "entry")

            return result["group_entry"]
        else:
            raise exceptions.MissingParamError("{} or {} must present".format('event_id', 'race_id', 'group_id'))

    def entry(self, entry_id):
        result = self.request("entry", entry_id)

        return result["entry"]

    # Results
    def results(self, event_id=None, race_id=None, bracket_id=None, interval_id=None):
        logger = logging.getLogger(self.log_filepath)

        if event_id is not None and race_id is not None:
            logger.warning("event_id ignored as race_id is suffuciaent to get the results")

        kwargs = {}
        if bracket_id:
            kwargs["bracket"] = bracket_id

        if interval_id:
            kwargs["interval"] = interval_id

        result = {}
        if race_id:
            result = self.request("race", race_id, "results", **kwargs)
            return result.get("race_results", [])
        elif event_id:
            result = self.request("event", event_id, "results", **kwargs)
            return result.get("event_results", [])
        elif bracket_id:
            # we dont care about bracket duplicating in query and path because API permits that. Which is strange
            result = self.request("bracket", bracket_id, "results", **kwargs)
            return result.get("bracket_results", [])
        elif interval_id:
            # strangely enough documentation says API for intervals does not support bracket as query param
            # but on practise it works. So bracket keeping bracket id
            result = self.request("interval", interval_id, "results", **kwargs)
            return result.get("iterval_results", [])
        else:
            raise exceptions.MissingParamError(
                "{} or {} or {} or {} must present".format('event_id', 'race_id', 'bracket_id', 'interval_id'))

    # Intervals
    def intervals(self, event_id=None, race_id=None):
        """
        Get all intervals of an event or race
        One and only one of the following parameters is required

        :param event_id: id of an event to get intervals by
        :param race_id: id of a race to get intervals by
        :return:
        """
        args = [event_id, race_id]
        if args.count(None) != 1:
            exceptions.InvalidCallError("Only one of {} {} must present".format('event_id', 'race_id'))

        result = []
        if event_id:
            result = self.request("event", event_id, "interval")

            return result.get("event_interval", [])
        elif race_id:
            result = self.request("race", race_id, "interval")

            return result.get("race_interval", [])
        else:
            raise exceptions.MissingParamError("{} or {} must present".format('event_id', 'race_id'))

    def interval(self, interval_id):
        result = self.request("interval", interval_id)

        return result.get("interval", {})

    # Brackets
    def brackets(self, event_id=None, race_id=None):
        """
        Get all brackets of event or race
        One and only one of the following parameters is required

        :param event_id: id of an event to get brackets by
        :param race_id: id of a race to get brackets by
        :return:
        """
        args = [event_id, race_id]
        if args.count(None) != 1:
            exceptions.InvalidCallError("Only one of {} {} must present".format('event_id', 'race_id'))

        if event_id:
            result = self.request("event", event_id, "bracket")

            return result.get("event_bracket", [])
        elif race_id:
            result = self.request("race", race_id, "bracket")

            return result.get("race_bracket", [])
        else:
            raise exceptions.MissingParamError("{} or {} must present".format('event_id', 'race_id'))

    def bracket(self, bracket_id):
        """
        Get bracket info
        """
        result = self.request("bracket", bracket_id)

        return result.get("bracket", {})

    # Waves
    def waves(self, event_id=None, race_id=None):
        """
        Get all waves of an event or race
        One and only one of the following parameters is required

        :param event_id: id of an event to get waves by
        :param race_id: id of a race to get waves by
        :return:
        """
        args = [event_id, race_id]
        if args.count(None) != 1:
            exceptions.InvalidCallError("Only one of {} {} must present".format('event_id', 'race_id'))

        result = []
        if event_id:
            result = self.request("event", event_id, "wave")
        elif race_id:
            result = self.request("race", race_id, "wave")
        else:
            raise exceptions.MissingParamError("{} or {} must present".format('event_id', 'race_id'))

        return result

    def wave(self, wave_id):
        """
        Get wave info
        :param wave_id: id of a wave
        :return:
        """
        result = self.request("wave", wave_id)

        return result

    # Timing points
    def timing_points(self, event_id=None, race_id=None, interval_id=None):
        """
        Get all timing points of an event, race or interval
        One and only one of the following parameters is required

        :param event_id: Event id to get timing points by
        :param race_id: Race id to get timing points by
        :param interval_id: Interval id to get timing points by
        :return:
        """
        args = [event_id, race_id, interval_id]
        if args.count(None) != 2:
            exceptions.InvalidCallError("Only one of {} {} {} must present".format('event_id', 'race_id', 'interval_id'))

        result = {}
        if event_id is not None:
            result = self.request("event", event_id, "timing-point")
        elif race_id is not None:
            result = self.request("race", race_id, "timing-point")
        elif interval_id is not None:
            result = self.request("interval", interval_id, "timing-point")
        else:
            raise exceptions.MissingParamError("{} or {} or {} must present".format('event_id', 'race_id', 'interval_id'))

        return result

    def timing_point(self, timing_point_id):
        result = self.request("timing-point", timing_point_id)

        return result

    # Timing devices
    def timing_devices(self, event_id=None, race_id=None, interval_id=None, timing_point_id=None):
        """
        Get all timing devices of an event, race, interval or timing point
        One and only one of the following parameters is required

        :param event_id: Event id to get timing devices by
        :param race_id: Race id to get timing devices by
        :param interval_id: Interval id to get timing devices by
        :param timing_point_id: Timing point id to get timing devices by
        :return:
        """
        args = [event_id, race_id, interval_id, timing_point_id]
        if args.count(None) != 3:
            exceptions.InvalidCallError("Only one of {} {} {} {} must present".format('event_id', 'race_id', 'interval_id', 'timing_point_id'))

        result = {}
        if event_id is not None:
            result = self.request("event", event_id, "timing-device")
        elif race_id is not None:
            result = self.request("race", race_id, "timing-device")
        elif interval_id is not None:
            result = self.request("interval", interval_id, "timing-device")
        elif timing_point_id is not None:
            result = self.request("timing-point", timing_point_id, "timing-device")
        else:
            raise exceptions.MissingParamError("{} or {} or {} or {} must present".format('event_id', 'race_id', 'interval_id', 'timing_point_id'))

        return result

    def timing_device(self, timing_device_id=None):
        result = self.request("timing-device", timing_device_id)

        return result

    # Timing mats
    def timing_mats(self, timing_device_id):
        """
        Get timing mats by id of timing device
        :param timing_device_id: id of timing device
        :return:
        """
        result = self.request("timing-device", timing_device_id, "timing-mat")

        return result

    def timing_mat(self, timing_mat_id):
        """
        Get timing mat info
        :param timing_mat_id: Id of timing mat
        :return:
        """
        result = self.request("timing-mat", timing_mat_id)

        return result

    # Groups
    def groups(self, event_id=None, entry_id=None):
        args = [event_id, entry_id]
        if args.count(None) != 1:
            exceptions.InvalidCallError("Only one of {} {} must present".format('event_id', 'entry_id'))

        result = {}
        if event_id is not None:
            result = self.request("event", event_id, "groups")
        elif entry_id is not None:
            result = self.request("entry", entry_id, "groups")
        else:
            raise exceptions.MissingParamError("{} or {} must present".format('event_id', 'entry_id'))

        return result

    def group(self, group_id):
        result = self.request("groups", group_id)

        return result


















