#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'
import re
import socket
import requests
from collections import namedtuple

import utils
from exceptions import RequetsHostException

# module: TL-WR720N
# match_type: 0/1/2, 0 -> equal; 1 -> has; 2 -> regEx(retain)
# exploit: available exploit list
from template.interpreter import result_queue

WFingerprint = namedtuple('w_fp', ['module', 'match_type', 'fp', 'exploit'])
# www_auth_fingerprint = namedtuple('r_fp', ['module', 'match_type', 'fp', 'exploit'])
# module: DIR-629
# segment: headers.server/body
# fp_type: 0/1/2, 0 -> equal; 1 -> has; 2 -> regEx(retain)
# fp: <a href="http://support.dlink.com" target="_blank">DIR-629</a>
# extra: [('<span class="version">.+?: (.+?)</span>', 1), ('style="text-transform:uppercase;">(.+?)</span>', 1)]
# exploit: available exploit list
ExtraInfo = namedtuple('extra', ['segment', 'feature', 'index'])
HFingerprint = namedtuple('h_fp', ['module', 'segment', 'match_type', 'fp', 'extra', 'exploit'])
JFeature = namedtuple('j_feature', ['feature', 'appendix'])
RouterInfo = namedtuple('router', ['host', 'port', 'brand', 'module', 'extra', 'exploit'])
FingerprintConf = namedtuple('fingerprint_conf', ['brand', 'www_auth_fp', 'http_fp'])

FINGERPRINT_DB = []
JUMP_FEATURES = []


class BaseScanner(object):
    __info__ = {}
    prompt = ''
    FINGERPRINT_DB = []
    JUMP_FEATURES = []

    def __init__(self):
        result_queue.empty()

    def ping(self, host, port, timeout):
        try:
            cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cs.settimeout(timeout)
            status = cs.connect((host, port))
            cs.close()
        except socket.error as msg:
            # print('Failed to connect host: {}. Error msg: {}'.format(host, msg))
            return False

        if status != 0:
            # return 0 means ping success
            return True
        else:
            return False

    def http_get(self, s, host, port, timeout, appendix=''):
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

    def scan(self, host, port, timeout):
        result = None
        if not self.ping(host, int(port), timeout):
            utils.print_warning('{}:{} requests error, msg: PingError'.format(host, port))
            return
        s = requests.Session()
        r1, err = self.http_get(s, host, port, timeout * 2)
        if err:
            utils.print_warning(err)
            return

        if 'WWW-Authenticate' in r1.headers:
            # match www_auth_fingerprint list
            brand, module_name, exploit = self.www_auth_handler(r1)
            if brand:
                result = RouterInfo(host=host, port=port, brand=brand, module=module_name, extra=None, exploit=exploit)
                utils.print_info("{}: {} {}".format(host, brand, module_name))
            else:
                # result = router(host=host, port=port, brand='Unknown', module='Unknown')
                utils.print_info("{}: {}".format(host, 'Unknown'))
                return

        else:
            for jp_list in self.JUMP_FEATURES:
                for jp_feature in jp_list:
                    jp_feature = JFeature._make(jp_feature)
                    if jp_feature.feature in r1.text:
                        # match jump_fingerprint list
                        appendix = jp_feature.appendix
                        r1, err = self.http_get(s, host, port, timeout * 2, appendix=appendix)
                        if err:
                            utils.print_warning(err)
                            return
            # match normal_fingerprint list
            brand, module_name, extra, exploit = self.http_auth_handler(r1)
            if brand:
                result = RouterInfo(host=host, port=port, brand=brand, module=module_name, extra=extra, exploit=exploit)
                if extra:
                    utils.print_info("{}: {} {}, {}".format(host, brand, module_name, extra))
                else:
                    utils.print_info("{}: {} {}".format(host, brand, module_name))
            else:
                utils.print_info("{}: {}".format(host, 'Unknown'))
                return

        result_queue.put(result)

    def www_auth_handler(self, r):
        for fp_conf in self.FINGERPRINT_DB:
            # fingerprint_conf = namedtuple('fingerprint_conf', ['brand', 'www_auth_fp', 'http_fp'])
            for r_fp in fp_conf.www_auth_fp:
                # fp_type: 0/1/2, 0 -> equal; 1 -> has; 2 -> regEx(retain)
                if r_fp.match_type == 0:
                    if r.headers['WWW-Authenticate'] == r_fp.fp:
                        return fp_conf.brand, r_fp.module, r_fp.exploit
                elif r_fp.match_type == 1:
                    if r_fp.fp in r.headers['WWW-Authenticate']:
                        return fp_conf.brand, r_fp.module, r_fp.exploit
                elif r_fp.match_type == 2:
                    pass

            if fp_conf.brand.lower() in r.headers['WWW-Authenticate'].lower():
                return fp_conf.brand, 'perhaps', []

        return None, None, None

    def http_auth_handler(self, r):
        for fp_conf in self.FINGERPRINT_DB:
            for r_fp in fp_conf.http_fp:
                # http_fingerprint = namedtuple('h_fp', ['module', 'segment', 'match_type', 'fp', 'extra', 'exploit'])
                if r_fp.segment.upper() == 'TEXT':
                    if self.grab_info(r.text, r_fp.match_type, r_fp.fp):
                        extra_info = self.grab_extra(r, r_fp.extra)
                        return fp_conf.brand, r_fp.module, extra_info, []
                else:
                    if r_fp.segment in r.headers:
                        if self.grab_info(r.headers[r_fp.segment], r_fp.match_type, r_fp.fp):
                            extra_info = self.grab_extra(r, r_fp.extra)
                            return fp_conf.brand, r_fp.module, extra_info, []

            if 'Server' in r.headers:
                if fp_conf.brand.lower() in r.headers['Server'].lower():
                    return fp_conf.brand, 'perhaps', None, []

            if fp_conf.brand.lower() in r.text.lower():
                return fp_conf.brand, 'perhaps', None, []

        return None, None, None, None

    def grab_info(self, raw, match_type, feature, index=None):
        if match_type == 0:
            if feature == raw:
                return True
        elif match_type == 1:
            if feature in raw:
                return True
        elif match_type == 2:
            regex = re.compile(feature)
            if_match = regex.search(raw)
            if if_match:
                if index is not None:
                    return if_match.group(index)
                else:
                    return True

        return False

    def grab_extra(self, r, extra_features):
        # extra(segment, feature, index)
        extra = []
        if extra_features[0]:
            # firmware
            extra_info = ExtraInfo._make(extra_features[0])
            if extra_info.segment.upper() == 'TEXT':
                info = self.grab_info(r.text, 2, extra_info.feature, extra_info.index)
            else:
                if extra_info.segment in r.headers:
                    info = self.grab_info(r.headers[extra_info.segment], 2, extra_info.feature, extra_info.index)
                else:
                    info = None

            if info:
                extra.append('firmware: {}'.format(info))

        if extra_features[1]:
            # hardware
            extra_info = ExtraInfo._make(extra_features[1])
            if extra_info.segment.upper() == 'TEXT':
                info = self.grab_info(r.text, 2, extra_info.feature, extra_info.index)
            else:
                if extra_info.segment in r.headers:
                    info = self.grab_info(r.headers[extra_info.segment], 2, extra_info.feature, extra_info.index)
                else:
                    info = None

            if info:
                extra.append('hardware: {}'.format(info))

        if len(extra) > 0:
            return ' '.join(extra)
        else:
            return None
