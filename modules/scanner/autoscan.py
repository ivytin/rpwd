#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'

import requests
import utils
from template.scanner import BaseScanner


class Scanner(BaseScanner):
    prompt = 'Autoscanner'

    @staticmethod
    def scan(host, port, timeout):
        if not Scanner.ping(host, int(port), timeout):
            utils.print_info('Connect to host: {}:{} failed'.format(host, port))
            return False
        s = requests.Session()
        r1, err = Scanner.http_get(s, host, port, timeout * 2)
        if err:
            utils.print_info(err)
            return

        if r1.status_code == requests.codes.unauthorized:
            module_name = Scanner.basic_auth_handler(r1)
            utils.print_info("{}: {}".format(host, module_name))
        else:
            module_name = Scanner.http_auth_handler(s, r1)
            utils.print_info("{}: {}".format(host, module_name))

    @staticmethod
    def basic_auth_handler(r):
        return r.headers['WWW-Authenticate']

    @staticmethod
    def http_auth_handler(s, r):
        return r.headers['Server']
