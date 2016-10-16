#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'

from template.scanner import WFingerprint, HFingerprint, BaseScanner, FingerprintConf

BASIC_FP = [
    WFingerprint('ZXV10 W300', 0, 'Basic realm="ZXV10 W300"', ['zynos.rom-0']),
    WFingerprint('ZXHN H108L', 0, 'Basic realm="ZXHN H108L"', ['zte.h108l_rce'])
]

HTTP_FP = [
    HFingerprint('F412', 'TEXT', 1, '<title>F412</title>', [None, None], []),
    HFingerprint('F460', 'TEXT', 1, '<title>F460</title>', [None, None], ['zte.f460_f660_rce']),
    HFingerprint('ZXA10 F460', 'TEXT', 1, '<title>ZXA10F460</title>', [None, None], ['zte.f460_f660_rce']),
    HFingerprint('F620', 'TEXT', 1, '<title>F620</title>', [None, None], []),
    HFingerprint('F620G', 'TEXT', 1, '<title>F620G</title>', [None, None], []),
    HFingerprint('F660', 'TEXT', 1, '<title>F660</title>', [None, None], ['zte.f460_f660_rce']),
    HFingerprint('MT-PON-AT-4', 'TEXT', 1, '<title>MT-PON-AT-4</title>', [None, None], []),
    HFingerprint('ZXDSL 931WII', 'TEXT', 1, '<title>ZXDSL 931WII</title>', [None, None], []),
    HFingerprint('ZXHN E5501', 'TEXT', 1, '<title>ZXHN E5501</title>', [None, None], []),
    HFingerprint('ZXHN E5502', 'TEXT', 1, '<title>ZXHN E5502</title>', [None, None], []),
    HFingerprint('ZXHN H168M', 'TEXT', 1, '<title>ZXHN H168M</title>', [None, None], []),
    HFingerprint('ZXHN H168N', 'TEXT', 1, '<title>ZXHN H168N</title>', [None, None], []),
    HFingerprint('ZXHN H208N', 'TEXT', 1, '<title>ZXHN H208N</title>', [None, None], []),
    HFingerprint('ZXHN H367N', 'TEXT', 1, '<title>ZXHN H367N</title>', [None, None], []),
    HFingerprint('ZXV10 H108L', 'TEXT', 1, '<title>ZXV10 H108L</title>', [None, None], []),
    HFingerprint('ZXV10 W300', 'TEXT', 1, '<title>ZXV10 W300</title>', [None, None], []),
    HFingerprint('ZXV10 H108L', 'TEXT', 1, '<title>ZXV10 H108L</title>', [None, None], []),
]

JUMP_LIST = []


class Scanner(BaseScanner):
    prompt = 'ZTE Scanner'
    FINGERPRINT_DB = [
        FingerprintConf('ZTE', BASIC_FP, HTTP_FP),
    ]

    JUMP_FEATURES = [JUMP_LIST]
