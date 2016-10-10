#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'

from template.scanner import BaseScanner, FingerprintConf
from modules.scanner import (
    tplink, netgear, dlink, asus, zte, linksys)


class Scanner(BaseScanner):
    prompt = 'AutoScanner'
    FINGERPRINT_DB = [
        FingerprintConf('TP-LINK', tplink.BASIC_FP, tplink.HTTP_FP),
        FingerprintConf('NETGEAR', netgear.BASIC_FP, netgear.HTTP_FP),
        FingerprintConf('D-LINK', dlink.BASIC_FP, dlink.HTTP_FP),
        FingerprintConf('ASUS', asus.BASIC_FP, asus.HTTP_FP),
        FingerprintConf('ZTE', zte.BASIC_FP, zte.HTTP_FP),
        FingerprintConf('LINKSYS', linksys.BASIC_FP, linksys.HTTP_FP)
    ]

    JUMP_FEATURES = [
        tplink.JUMP_LIST, netgear.JUMP_LIST, dlink.JUMP_LIST,
        asus.JUMP_LIST, zte.JUMP_LIST, linksys.JUMP_LIST]

