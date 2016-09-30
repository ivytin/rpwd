#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'

from template.scanner import WFingerprint, HFingerprint

# WFingerprint = namedtuple('w_fp', ['module', 'match_type', 'fp', 'exploit'])
BASIC_FP = [
    WFingerprint('DCS-910', 0, 'BASIC realm=DCS-910', []),
    WFingerprint('DIR-300', 0, 'Basic realm="D-Link DIR-300"', []),
    WFingerprint('DIR-320', 0, 'Basic realm="D-Link DIR-320"', []),
    WFingerprint('DCS-2000', 0, 'Basic realm="DCS-2000"', []),
    WFingerprint('DCS-2100+', 0, 'Basic realm="DCS-2100+"', []),
    WFingerprint('DCS-2100G', 0, 'Basic realm="DCS-2100G"', []),
    WFingerprint('DCS-2103', 0, 'Basic realm="DCS-2103"', []),
    WFingerprint('DCS-2132L', 0, 'Basic realm="DCS-2132L"', []),
    WFingerprint('DCS-2132LB1', 0, 'Basic realm="DCS-2132LB1"', []),
    WFingerprint('DCS-2210', 0, 'Basic realm="DCS-2210"', []),
    WFingerprint('DCS-2230', 0, 'Basic realm="DCS-2230"', []),
    WFingerprint('DCS-5020L', 0, 'Basic realm="DCS-5020L"', []),
    WFingerprint('DCS-5300', 0, 'Basic realm="DCS-5300"', []),
    WFingerprint('DCS-5300W', 0, 'Basic realm="DCS-5300W"', []),
    WFingerprint('DCS-6620G', 0, 'Basic realm="DCS-6620G"', []),
    WFingerprint('DCS-6817', 0, 'Basic realm="DCS-6817"', []),
    WFingerprint('DCS-930', 0, 'Basic realm="DCS-930"', []),
    WFingerprint('DCS-930L', 0, 'Basic realm="DCS-930L"', []),
    WFingerprint('DCS-930LB1', 0, 'Basic realm="DCS-930LB1"', []),
    WFingerprint('DCS-932L', 0, 'Basic realm="DCS-932L"', []),
    WFingerprint('DCS-933L', 0, 'Basic realm="DCS-933L"', []),
    WFingerprint('DI-524', 0, 'Basic realm="DI-524"', []),
    WFingerprint('DI-604', 0, 'Basic realm="DI-604"', []),
    WFingerprint('DI-624', 0, 'Basic realm="DI-624"', []),
    WFingerprint('DI-704P', 0, 'Basic realm="DI-704P"', []),
    WFingerprint('DI-707P', 0, 'Basic realm="DI-707P"', []),
    WFingerprint('DI-804HV', 0, 'Basic realm="DI-804HV"', []),
    WFingerprint('DI-808HV', 0, 'Basic realm="DI-808HV"', []),
    WFingerprint('DI-824VUP', 0, 'Basic realm="DI-824VUP"', []),
    WFingerprint('DI-824VUP+', 0, 'Basic realm="DI-824VUP+"', []),
    WFingerprint('DIR-100', 0, 'Basic realm="DIR-100"', []),
    WFingerprint('DIR-130', 0, 'Basic realm="DIR-130"', []),
    WFingerprint('DIR-330', 0, 'Basic realm="DIR-330"', []),
    WFingerprint('DIR-400', 0, 'Basic realm="DIR-400"', []),
    WFingerprint('DIR-615 Rev.E3', 0, 'Basic realm="DIR-615 Rev.E3"', []),
    WFingerprint('DIR-615"', 0, 'Basic realm="DIR-615"', []),
    WFingerprint('DIR-825', 0, 'Basic realm="DIR-825"', []),
    WFingerprint('DSL-2600U', 0, 'Basic realm="DSL-2600U"', []),
    WFingerprint('DSL-2740R', 0, 'Basic realm="DSL-2740R"', []),
    WFingerprint('DSL-320B', 0, 'Basic realm="DSL-320B"', []),
    WFingerprint('DSL-321B', 0, 'Basic realm="DSL-321B"', []),
    WFingerprint('DWL-2000AP+', 0, 'Basic realm="DWL-2000AP+"', []),
    WFingerprint('DWL-G700AP', 0, 'Basic realm="DWL-G700AP Login"', []),
    WFingerprint('DWL-G700AP', 0, 'Basic realm="DWL-G700AP"', []),
    WFingerprint('N300', 0, 'Basic realm="Wireless N300 Router"', []),
    WFingerprint('DI-604', 1, 'Digest realm="DI-604"', []),
    WFingerprint('DI-624', 1, 'Digest realm="DI-624"', []),
]

# http_fingerprint = namedtuple('h_fp', ['module', 'segment', 'math_type', 'fp', 'extra', 'exploit'])
HTTP_FP = [
    HFingerprint('DAP-1522', 'Server', 1, 'DAP-1522', [('Server', 'Ver .+', 0), None], []),
]

JUMP_LIST = []

