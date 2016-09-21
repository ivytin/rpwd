#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'
import socket
import utils


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
