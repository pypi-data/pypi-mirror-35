# Vacasa API
# Copyright 2018 John W. Miller
# See LICENSE for details.

"""
API details and documentation: https://vacasa.docs.stoplight.io/
"""

import requests
import socket
import time


class API(object):
    """Vacasa API"""

    # Create a persistent requests connection
    session = requests.Session()
    session.headers = {"Application": "vacasa_python_client"}

    def __init__(self, api_key, api_secret, timeout=5, sleep_time=1.5):
        """ Vacasa API Constructor

        :param api_key: API key provided by Vacasa (str)
        :param api_secret: API secret provided by Vacasa (str)
        :param timeout: time before quitting on response (seconds)
        :param sleep_time: time to wait between requests (seconds)
        :param allow_extra_calls: override the API call limit (bool)
        """

        assert api_key != '', 'Must supply a non-empty API key.'
        assert api_secret != '', 'Must supply a non-empty API secret.'
        self.auth = {'key': api_key, 'secret': api_secret}
        self.host = "connect.vacasa.com/"
        self.timeout = timeout
        self.sleep_time = max(sleep_time, 1)  # Rate limiting

    def _make_request(self, path,
                      method='GET',
                      query_=None,
                      params_=None,
                      json_=None):
        """ Make a request to the API """

        try:
            uri = self.api_root + path
            response = self.session.request(method, uri,
                                            timeout=self.timeout,
                                            data=query_,
                                            params=params_,
                                            json=json_)
        except socket.timeout as e:
            print("Timeout raised and caught: {}".format(e))
            return

        time.sleep(self.sleep_time)  # Enforce rate limiting
        return response
