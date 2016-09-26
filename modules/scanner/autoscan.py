#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'

import requests
import utils
from collections import namedtuple
from template.scanner import BaseScanner, router
from template.interpreter import result_queue
from modules.scanner import tplink

fingerprint_conf = namedtuple('fingerprint_conf', ['brand', 'basic_fp', 'http_auth'])

FINGERPRINT_DB = [
    fingerprint_conf('TP-LINK', tplink.BASIC_FP, tplink.HTTP_FP),
]


class Scanner(BaseScanner):
    prompt = 'Autoscanner'

    @staticmethod
    def scan(host, port, timeout):
        results = []
        if not Scanner.ping(host, int(port), timeout):
            utils.print_warning('{}:{} requests error, msg: PingError'.format(host, port))
            return False
        s = requests.Session()
        r1, err = Scanner.http_get(s, host, port, timeout * 2)
        if err:
            utils.print_warning(err)
            return

        if 'WWW-Authenticate' in r1.headers:
            brand, module_name = Scanner.basic_auth_handler(r1)
            if brand:
                results.append(router(host=host, port=port, brand=brand, module=module_name))
                utils.print_info("{}: {} {}".format(host, brand, module_name))
            else:
                results.append(router(host=host, port=port, brand='Unknown', module='Unknown'))
                utils.print_info("{}: {} {}".format(host, brand, 'Unknown'))
        else:
            module_name = Scanner.http_auth_handler(s, r1)
            utils.print_info("{}: {}".format(host, module_name))

        for result in results:
            result_queue.put(result)

    @staticmethod
    def basic_auth_handler(r):
        for fp_conf in FINGERPRINT_DB:
            for r_fp in fp_conf.basic_fp:
                if r_fp.segment in r.headers and r.headers[r_fp.segment] == r_fp.fp:
                    return fp_conf.brand, r_fp.module

            if fp_conf.brand in r.headers['WWW-Authenticate']:
                return fp_conf.brand, 'perhaps'

        return None, None

    @staticmethod
    def http_auth_handler(s, r):
        return 'http'
