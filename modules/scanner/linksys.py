#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'

from template.scanner import WFingerprint, HFingerprint, BaseScanner, FingerprintConf

BASIC_FP = [
    WFingerprint('WRT610N', 0, 'Basic realm="WRT610N"', []),
    WFingerprint('E900', 0, 'Basic realm="E900"', []),
    WFingerprint('EA4500', 0, 'Basic realm="Linksys EA4500"', []),
    WFingerprint('WRP400', 0, 'Basic realm="WRP400"', []),
    WFingerprint('WRT54G', 0, 'Basic realm="WRT54G"', []),
    WFingerprint('WRT54G2', 0, 'Basic realm="WRT54G2"', []),
    WFingerprint('WRT54GC', 0, 'Basic realm="WRT54GC"', []),
    WFingerprint('WRT54GL', 0, 'Basic realm="WRT54GL"', []),
]

HTTP_FP = []

JUMP_LIST = []


class Scanner(BaseScanner):
    prompt = 'LINKSYS Scanner'
    FINGERPRINT_DB = [
        FingerprintConf('LINKSYS', BASIC_FP, HTTP_FP),
    ]

    JUMP_FEATURES = [JUMP_LIST]
