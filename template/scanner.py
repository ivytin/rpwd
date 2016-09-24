#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'

import socket
import requests

from exceptions import RequetsHostException


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
        except requests.ConnectTimeout:
            return None, RequetsHostException('HTTP connection timeout, host: http://{}:{}'
                                              .format(host, port))
        except requests.ConnectionError:
            return None, RequetsHostException('HTTP connection error, host: http://{}:{}'
                                              .format(host, port))
        except requests.HTTPError:
            return None, RequetsHostException('HTTP server response error, host: http://{}:{}'
                                              .format(host, port))
        except requests.exceptions.RequestException as msg:
            return None, RequetsHostException('call requests.get error, msg: {}'
                                              .format(msg))
        else:
            return r, None
