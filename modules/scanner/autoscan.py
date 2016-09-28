#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'

import requests
import utils
from collections import namedtuple
from template.scanner import BaseScanner, router
from template.interpreter import result_queue
from modules.scanner import tplink

fingerprint_conf = namedtuple('fingerprint_conf', ['brand', 'www_auth_fp', 'http_fp'])

FINGERPRINT_DB = [
    fingerprint_conf('TP-LINK', tplink.BASIC_FP, tplink.HTTP_FP),
]

JUMP_FEATURES = []


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
            brand, module_name, _ = Scanner.www_auth_handler(r1)
            if brand:
                result = router(host=host, port=port, brand=brand, module=module_name)
                utils.print_info("{}: {} {}".format(host, brand, module_name))
            else:
                # result = router(host=host, port=port, brand='Unknown', module='Unknown')
                utils.print_info("{}: {}".format(host, 'Unknown'))
                return

        else:
            for jp_feature in JUMP_FEATURES:
                if jp_feature in r1.text:
                    # match jump_fingerprint list
                    appendix = jp_feature
                    r1, err = Scanner.http_get(s, host, port, timeout * 2, appendix='')
                    if err:
                        utils.print_warning(err)
                        return
            # match normal_fingerprint list
                brand, module_name, extra, _ = Scanner.http_auth_handler(s, r1)
                if brand:
                    utils.print_info("{}: {}, {}".format(host, module_name, extra))
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
    def http_auth_handler(s, r):
        for fp_conf in FINGERPRINT_DB:
            for r_fp in fp_conf.http_fp:
                # http_fingerprint = namedtuple('h_fp', ['module', 'segment', 'math_type', 'fp', 'extra', 'exploit'])
                if r_fp.segment == 'TEXT':
                    pass
                else:
                    if r_fp.match_type == 0:
                        pass
                    elif r_fp.match_type == 1:
                         pass
                    elif r_fp.match_type == 2:
                        pass

            if fp_conf.brand.lower() in r.headers['Server'].lower():
                return fp_conf.brand, 'perhaps', None, []

        return None, None, None, None
