#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'

import logging


LOGGER = logging.getLogger(__name__)


class RouterPwnException(Exception):
    def __init__(self, msg=''):
        super(RouterPwnException, self).__init__(msg)
        # LOGGER.exception(self)


class ModuleImportException(RouterPwnException):
    pass


class BadHostInfoException(RouterPwnException):
    pass


class StopThreadPoolExecutor(RouterPwnException):
    pass


class RequetsHostException(RouterPwnException):
    pass
