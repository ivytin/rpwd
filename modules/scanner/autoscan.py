#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'
import re
import requests
import utils
from template.scanner import BaseScanner, RouterInfo, ExtraInfo, FingerprintConf, JFeature
from template.interpreter import result_queue
from modules.scanner import tplink, netgear, dlink

FINGERPRINT_DB = [
    FingerprintConf('TP-LINK', tplink.BASIC_FP, tplink.HTTP_FP),
    FingerprintConf('NETGEAR', netgear.BASIC_FP, netgear.HTTP_FP),
    FingerprintConf('D-LINK', dlink.BASIC_FP, dlink.HTTP_FP),
]

JUMP_FEATURES = [tplink.JUMP_LIST, netgear.JUMP_LIST]


class Scanner(BaseScanner):
    prompt = 'AutoScanner'

    @staticmethod
    def scan(host, port, timeout):
        result = None
        if not Scanner.ping(host, int(port), timeout):
            utils.print_warning('{}:{} requests error, msg: PingError'.format(host, port))
            return
        s = requests.Session()
        r1, err = Scanner.http_get(s, host, port, timeout * 2)
        if err:
            utils.print_warning(err)
            return

        if 'WWW-Authenticate' in r1.headers:
            # match www_auth_fingerprint list
            brand, module_name, exploit = Scanner.www_auth_handler(r1)
            if brand:
                result = RouterInfo(host=host, port=port, brand=brand, module=module_name, extra=None, exploit=exploit)
                utils.print_info("{}: {} {}".format(host, brand, module_name))
            else:
                # result = router(host=host, port=port, brand='Unknown', module='Unknown')
                utils.print_info("{}: {}".format(host, 'Unknown'))
                return

        else:
            for jp_list in JUMP_FEATURES:
                for jp_feature in jp_list:
                    jp_feature = JFeature._make(jp_feature)
                    if jp_feature.feature in r1.text:
                        # match jump_fingerprint list
                        appendix = jp_feature.appendix
                        r1, err = Scanner.http_get(s, host, port, timeout * 2, appendix=appendix)
                        if err:
                            utils.print_warning(err)
                            return
            # match normal_fingerprint list
            brand, module_name, extra, exploit = Scanner.http_auth_handler(r1)
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

    @staticmethod
    def www_auth_handler(r):
        for fp_conf in FINGERPRINT_DB:
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

    @staticmethod
    def http_auth_handler(r):
        for fp_conf in FINGERPRINT_DB:
            for r_fp in fp_conf.http_fp:
                # http_fingerprint = namedtuple('h_fp', ['module', 'segment', 'match_type', 'fp', 'extra', 'exploit'])
                if r_fp.segment.upper() == 'TEXT':
                    if Scanner.grab_info(r.text, r_fp.match_type, r_fp.fp):
                        extra_info = Scanner.grab_extra(r, r_fp.extra)
                        return fp_conf.brand, r_fp.module, extra_info, []
                else:
                    if r_fp.segment in r.headers:
                        if Scanner.grab_info(r.headers[r_fp.segment], r_fp.match_type, r_fp.fp):
                            extra_info = Scanner.grab_extra(r, r_fp.extra)
                            return fp_conf.brand, r_fp.module, extra_info, []

            if 'Server' in r.headers:
                if fp_conf.brand.lower() in r.headers['Server'].lower():
                    return fp_conf.brand, 'perhaps', None, []

            if fp_conf.brand.lower() in r.text.lower():
                return fp_conf.brand, 'perhaps', None, []

        return None, None, None, None

    @staticmethod
    def grab_info(raw, match_type, feature, index=None):
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

    @staticmethod
    def grab_extra(r, extra_features):
        # extra(segment, feature, index)
        extra = []
        if extra_features[0]:
            # firmware
            extra_info = ExtraInfo._make(extra_features[0])
            if extra_info.segment.upper() == 'TEXT':
                info = Scanner.grab_info(r.text, 2, extra_info.feature, extra_info.index)
            else:
                if extra_info.segment in r.headers:
                    info = Scanner.grab_info(r.headers[extra_info.segment], 2, extra_info.feature, extra_info.index)
                else:
                    info = None

            if info:
                extra.append('firmware: {}'.format(info))

        if extra_features[1]:
            # hardware
            extra_info = ExtraInfo._make(extra_features[1])
            if extra_info.segment.upper() == 'TEXT':
                info = Scanner.grab_info(r.text, 2, extra_info.feature, extra_info.index)
            else:
                if extra_info.segment in r.headers:
                    info = Scanner.grab_info(r.headers[extra_info.segment], 2, extra_info.feature, extra_info.index)
                else:
                    info = None

            if info:
                extra.append('hardware: {}'.format(info))

        if len(extra) > 0:
            return ' '.join(extra)
        else:
            return None
