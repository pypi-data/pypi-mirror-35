# system modules
import logging
import urllib
import json
import functools
import re

# internal modules
from sensemapi import paths
from sensemapi.reprobject import ReprObject
from sensemapi.senseBox import senseBox
from sensemapi.errors import *
from sensemapi.utils import *

# external modules
import requests

logger = logging.getLogger(__name__)

class SenseMapClient(ReprObject):
    """
    Client to interface the `OpenSenseMap API <https://api.opensensemap.org>`_
    """
    def _get_box(self, id, format = None):
        """
        Issue the request to retreive a single senseBox

        Args:
            id (str) : the senseBox id to retreive
            format (str, optional): one of ``"json"`` and ``"geojson"``

        Returns:
            dict : the API response
        """
        response = requests.get(
            urllib.parse.urljoin(paths.BOXES+"/",id),
            params = {"format":format} if format else {}
            )
        response_json = response.json()
        logger.debug("API responded JSON:\n{}".format(
            json.dumps(response_json, sort_keys = True, indent = 4)))
        if response.status_code == 200:
            return response_json
        else:
            message = response_json.get("message")
            raise OpenSenseMapAPIError("Could not retreive with id '{}'{}"
                .format(id, ": {}".format(message) if message else ""))

    def get_box(self, id):
        """
        Retreive one :any:`senseBox`

        Args:
            id (str) : the senseBox id to retreive

        Returns:
            senseBox : the retreived senseBox
        """
        box = senseBox.from_json(self._get_box(id = id, format = "json"))
        box.client = self
        return box

    def _post_measurement(self, box_id, sensor_id, value, time = None,
        lat = None, lon = None, height = None):
        """
        Issue a request to upload a new measurement

        Args:
            box_id (str) : the senseBox id
            sensor_id (str) : the sensor's id
            value (float) : the current measurement value
            time (datetime.datetime, optional) : the time of the measurement
            lat, lon, height (float,optional) : the current position

        Returns:
            True : on success
        """
        assert box_id is not None, "box_id must  be defined"
        assert sensor_id is not None, "sensor_id must  be defined"
        d = {}
        d["value"] = float(value)
        if time:
            d["createdAt"] = date2str(time)
        try:
            d["location"] = location_dict(lat, lon, height)
        except ValueError:
            pass
        logger.debug("Sending Request with JSON:\n{}"
            .format(pretty_json(d)))
        response = requests.post(
            functools.reduce(urllib.parse.urljoin,
                [paths.BOXES+"/",box_id+"/",sensor_id]),
            json = d,
            )
        response_json = response.json()
        logger.debug("API responded JSON:\n{}"
            .format(pretty_json(response_json)))
        if hasattr(response_json, "get"): # is a dict
            message = response_json.get("message")
            raise OpenSenseMapAPIError("Posting measurement didn't work{}"
                .format(": "+ message or ""))
        else: # no dict
            if re.search("measurement\s+saved\s+in\s+box",response_json):
                return True

    def post_measurement(self, sensor):
        """
        Upload the current measurement of a given :any:`senseBoxSensor`.

        Args:
            sensor (senseBoxSensor) : the sensor
        """
        assert sensor.id, "the given sensor does not have an id"
        assert sensor.box, "the given sensor does not know its senseBox"
        assert sensor.box.id, "the given sensor's senseBox does not have an id"
        assert sensor.last_value, "the given sensor does not have a last_value"
        post_kwargs = {}
        post_kwargs.update(
            box_id = sensor.box.id,
            sensor_id = sensor.id,
            value = float(sensor.last_value),
            )
        if sensor.box.exposure == "mobile":
            post_kwargs.update(
                lat = box.current_lat,
                lon = box.current_lon,
                height = box.current_height,
                )
        if sensor.last_time:
            post_kwargs.update(time = sensor.last_time)
        return self._post_measurement(**post_kwargs)
