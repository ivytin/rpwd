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
            utils.print_warning('Connect to host: {}:{} failed'.format(host, port))
            return False
        try:
            r = requests.get('http://{}:{}'.format(host, port), timeout=timeout)
        except requests.ConnectTimeout:
            utils.print_warning('HTTP get call to host: http://{}:{} timeout'.format(host, port))
            return False
        else:
            utils.print_info('host: http://{}:{} status code:{}'.format(host, port, r.status_code))

