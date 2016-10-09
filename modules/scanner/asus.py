#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'

from template.scanner import WFingerprint, HFingerprint, BaseScanner, FingerprintConf

BASIC_FP = [
    WFingerprint('AX-125', 0, 'Basic realm="AX-125', []),
    WFingerprint('"AX-112W', 0, 'Basic realm="AX-112W', []),
    WFingerprint('DSL-AC68U"', 0, 'Basic realm="DSL-AC68U"', []),
    WFingerprint('DSL-N10', 0, 'Basic realm="DSL-N10"', []),
    WFingerprint('DSL-N12U', 0, 'Basic realm="DSL-N12U"', []),
    WFingerprint('DSL-N12U-C1', 0, 'Basic realm="DSL-N12U-C1"', []),
    WFingerprint('DSL-N12U', 0, 'Basic realm="DSL-N12U"', []),
    WFingerprint('DSL-N12U-C1', 0, 'Basic realm="DSL-N12U-C1"', []),
    WFingerprint('DSL-N14U', 0, 'Basic realm="DSL-N14U"', []),
    WFingerprint('DSL-N16U', 0, 'Basic realm="DSL-N16U"', []),
    WFingerprint('DSL-N55U', 0, 'Basic realm="DSL-N55U"', []),
    WFingerprint('DSL-N55U-B', 0, 'Basic realm="DSL-N55U-B"', []),
    WFingerprint('DSL-N66U', 0, 'Basic realm="DSL-N66U"', []),
    WFingerprint('EA-N66', 0, 'Basic realm="EA-N66"', []),
    WFingerprint('RT-AC51U', 0, 'Basic realm="RT-AC51U"', []),
    WFingerprint('RT-AC52U', 0, 'Basic realm="RT-AC52U"', []),
    WFingerprint('RT-AC56U', 0, 'Basic realm="RT-AC56U"', []),
    WFingerprint('RT-AC66R', 0, 'Basic realm="RT-AC66R"', []),
    WFingerprint('RT-AC66U', 0, 'Basic realm="RT-AC66U"', []),
    WFingerprint('RT-AC68P', 0, 'Basic realm="RT-AC68P"', []),
    WFingerprint('RT-AC68U', 0, 'Basic realm="RT-AC68U"', []),
    WFingerprint('RT-AC87U', 0, 'Basic realm="RT-AC87U"', []),
    WFingerprint('RT-G32.C1', 0, 'Basic realm="RT-G32.C1"', []),
    WFingerprint('RT-G32', 0, 'Basic realm="RT-G32"', []),
    WFingerprint('RT-N10+', 0, 'Basic realm="RT-N10+"', []),
    WFingerprint('RT-N10', 0, 'Basic realm="RT-N10"', []),
    WFingerprint('RT-N10.C1', 0, 'Basic realm="RT-N10.C1"', []),
    WFingerprint('RT-N10E', 0, 'Basic realm="RT-N10E"', []),
    WFingerprint('RT-N10LX', 0, 'Basic realm="RT-N10LX"', []),
    WFingerprint('RT-N10P', 0, 'Basic realm="RT-N10P"', []),
    WFingerprint('RT-N10U', 0, 'Basic realm="RT-N10U"', []),
    WFingerprint('RT-N11', 0, 'Basic realm="RT-N11"', []),
    WFingerprint('RT-N11P', 0, 'Basic realm="RT-N11P"', []),
    WFingerprint('RT-N12', 0, 'Basic realm="RT-N12"', []),
    WFingerprint('RT-N12+', 0, 'Basic realm="RT-N12+"', []),
    WFingerprint('RT-N12E', 0, 'Basic realm="RT-N12E"', []),
    WFingerprint('RT-N12LX', 0, 'Basic realm="RT-N12LX"', []),
    WFingerprint('RT-N12VP', 0, 'Basic realm="RT-N12VP"', []),
    WFingerprint('RT-N12-B1', 0, 'Basic realm="RT-N12-B1"', []),
    WFingerprint('RT-N12-C1', 0, 'Basic realm="RT-N12-C1"', []),
    WFingerprint('RT-N12-D1', 0, 'Basic realm="RT-N12-D1"', []),
    WFingerprint('RT-N13', 0, 'Basic realm="RT-N13"', []),
    WFingerprint('RT-N13U', 0, 'Basic realm="RT-N13U"', []),
    WFingerprint('RT-N13U-B1', 0, 'Basic realm="RT-N13U-B1"', []),
    WFingerprint('RT-N14U', 0, 'Basic realm="RT-N14U"', []),
    WFingerprint('RT-N15', 0, 'Basic realm="RT-N15"', []),
    WFingerprint('RT-N15U', 0, 'Basic realm="RT-N15U"', []),
    WFingerprint('RT-N16', 0, 'Basic realm="RT-N16"', []),
    WFingerprint('RT-N18U', 0, 'Basic realm="RT-N18U"', []),
    WFingerprint('RT-N53', 0, 'Basic realm="RT-N53"', []),
    WFingerprint('RT-N56U', 0, 'Basic realm="RT-N56U"', []),
    WFingerprint('RT-N65U', 0, 'Basic realm="RT-N65U"', []),
    WFingerprint('RT-N66R', 0, 'Basic realm="RT-N66R"', []),
    WFingerprint('RT-N66U', 0, 'Basic realm="RT-N66U"', []),
    WFingerprint('RT-N66W', 0, 'Basic realm="RT-N66W"', []),
    WFingerprint('RX3041 V2', 0, 'Basic realm="RX3041 V2"', []),
    WFingerprint('RX3041', 0, 'Basic realm="RX3041"', []),
    WFingerprint('RX3041H', 0, 'Basic realm="RX3041H"', []),
    WFingerprint('WL-300', 1, 'Basic realm="WL-300', []),
    WFingerprint('WL-320', 1, 'Basic realm="WL-320', []),
    WFingerprint('WL-330N', 0, 'Basic realm="WL-330N"', []),
    WFingerprint('WL-330N3G', 0, 'Basic realm="WL-330N3G"', []),
    WFingerprint('WL-500W', 0, 'Basic realm="ASUS WL-500W"', []),
    WFingerprint('WL-500gP V2', 0, 'Basic realm="WL-500gP V2"', []),
    WFingerprint('WL-500gP', 0, 'Basic realm="ASUS WL-500gP"', []),
    WFingerprint('WL-520gc', 0, 'Basic realm="ASUS WL-520gc"', []),
    WFingerprint('WL-520GU', 0, 'Basic realm="WL-520GU"', []),
]

HTTP_FP = []

JUMP_LIST = []


class Scanner(BaseScanner):
    prompt = 'ASUS Scanner'
    FINGERPRINT_DB = [
        FingerprintConf('ASUS', BASIC_FP, HTTP_FP),
    ]

    JUMP_FEATURES = [JUMP_LIST]
