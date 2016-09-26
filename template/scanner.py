#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'

import socket
import requests
from collections import namedtuple
from exceptions import RequetsHostException

router_fingerprint = namedtuple('r_fingerprint', ['module', 'segment', 'fp', 'exploit'])
router = namedtuple('router', ['host', 'port', 'brand', 'module'])


class BaseScanner(object):
    __info__ = {}

    def run(self):
        pass

    def check(self):
        pass

    @staticmethod
    def ping(host, port, timeout):
        try:
            cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cs.settimeout(timeout)
            status = cs.connect((host, port))
        except socket.error as msg:
            # print('Failed to connect host: {}. Error msg: {}'.format(host, msg))
            return False

        if status != 0:
            # return 0 means ping success
            return True
        else:
            return False

    @staticmethod
    def http_get(s, host, port, timeout):
        try:
            r = s.get('http://{}:{}'.format(host, port), timeout=timeout, verify=False)
        # except requests.exceptions.Timeout:
        #     return None, RequetsHostException('HTTP connection timeout, host: http://{}:{}'
        #                                       .format(host, port))
        except requests.RequestException as err:
            return None, RequetsHostException('{}:{} request error, msg: {}'
                                              .format(host, port, type(err).__name__))
        # except requests.HTTPError:
        #     return None, RequetsHostException('HTTP server response error, host: http://{}:{}'
        #                                       .format(host, port))
        # except requests.exceptions.RequestException as msg:
        #     return None, RequetsHostException('call requests.get error, msg: {}'
        #                                       .format(msg))
        else:
            return r, None
