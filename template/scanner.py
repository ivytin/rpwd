#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'

import socket
import requests
from collections import namedtuple
from exceptions import RequetsHostException

# module: TL-WR720N
# match_type: 0/1/2, 0 -> equal; 1 -> has; 2 -> regEx(retain)
# exploit: available exploit list

www_fingerprint = namedtuple('w_fp', ['module', 'match_type', 'fp', 'exploit'])
# www_auth_fingerprint = namedtuple('r_fp', ['module', 'match_type', 'fp', 'exploit'])
# module: DIR-629
# segment: headers.server/body
# fp_type: 0/1/2, 0 -> equal; 1 -> has; 2 -> regEx(retain)
# fp: <a href="http://support.dlink.com" target="_blank">DIR-629</a>
# extra: [('<span class="version">.+?: (.+?)</span>', 1), ('style="text-transform:uppercase;">(.+?)</span>', 1)]
# exploit: available exploit list
http_fingerprint = namedtuple('h_fp', ['module', 'segment', 'match_type', 'fp', 'extra', 'exploit'])
# http_fingerprint = namedtuple('h_fp', ['module', 'segment', 'match-type', 'fp', [('', '', 1), ('', '', 1)], []])
jump_feature = {
    '': [],
    # '': []
}
router = namedtuple('router', ['host', 'port', 'brand', 'module', 'extra', 'exploit'])


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
    def http_get(s, host, port, timeout, appendix=''):
        try:
            r = s.get('http://{}:{}{}'.format(host, port, appendix), timeout=timeout, verify=False)
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
