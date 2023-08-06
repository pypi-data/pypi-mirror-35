# coding: utf-8 2018/9/4 13:44
import json
import sys
from pprint import pprint

from .globals import url

import requests
from requests import ConnectTimeout


class HttpClient(object):

    def __init__(self):
        self.timeout = 5

    def send_request(self, params):
        full_url = url + "?" + params
        print(full_url)
        session = requests.Session()
        try:
            resp = session.get(full_url, verify=True, timeout=self.timeout)
        except ConnectTimeout as tmot:
            print("connect timeout={}".format(self.timeout))
            sys.exit(-1)
        contents = resp.text
        # pprint(json.loads(contents), indent=2)
        print(contents)
        return contents
