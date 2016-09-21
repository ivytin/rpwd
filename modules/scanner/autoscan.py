#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'

import requests
import utils
from exceptions import RequetsHostException
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
        else:
            module_name = Scanner.http_auth_handler(s, r1)

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

    @staticmethod
    def basic_auth_handler(r):
        utils.print_info(r.headers['WWW-Authenticate'])
        return True

    @staticmethod
    def http_auth_handler(s, r):
        utils.print_info(r.headers['Server'])
        return True
