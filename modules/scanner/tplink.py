#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'

from template.scanner import WFingerprint, HFingerprint, BaseScanner, FingerprintConf

# www_fingerprint = namedtuple('w_fp', ['module', 'match_type', 'fp', 'exploit'])
BASIC_FP = [
    WFingerprint('R860', 0, 'Basic realm="TP-LINK Router R860"', []),
    WFingerprint('WR720N', 0, 'Basic realm="150Mbps Wireless N Router TL-WR720N"', []),
    WFingerprint('TD-8816', 0, 'Basic realm="TD-8816"', ['zynos.rom-0']),
    WFingerprint('TD-8840T 2.0', 0, 'Basic realm="TD-8840T 2.0"', []),
    WFingerprint('TD-8840T', 0, 'Basic realm="TD-8840T"', []),
    WFingerprint('TL-WR841HP', 0, 'Basic realm="TP-LINK 300Mbps High Power Wireless N Router TL-WR841HP"', []),
    WFingerprint('TD-VG3631', 0, 'Basic realm="TP-LINK 300Mbps Wireless N VoIP ADSL2+ Modem Router TD-VG3631"', []),
    WFingerprint('Archer C5', 0, 'Basic realm="TP-LINK AC1200 Wireless Dual Band Gigabit Router Archer C5"', []),
    WFingerprint('Archer C8', 0, 'Basic realm="TP-LINK AC1750 Wireless Dual Band Gigabit Router Archer C8"', []),
    WFingerprint('Archer C9', 0, 'Basic realm="TP-LINK AC1750 Wireless Dual Band Gigabit Router Archer C9"', []),
    WFingerprint('TD-8840T', 0, 'Basic realm="TP-LINK ADSL2+ Modem Router TD-8840T"', []),
    WFingerprint('R600VPN', 0, 'Basic realm="TP-LINK Gigabit Broadband VPN Router R600VPN"', []),
    WFingerprint('WR842ND', 0, 'Basic realm="TP-LINK Multi-Function Wireless N Router WR842ND"', []),
    WFingerprint('WA7210N', 0, 'Basic realm="TP-LINK Outdoor Wireless Access Point WA7210N"', []),
    WFingerprint('MR3020', 0, 'Basic realm="TP-LINK Portable Wireless N 3G/4G Router MR3020"', []),
    WFingerprint('MR3040', 0, 'Basic realm="TP-LINK Portable Wireless N 3G/4G Router MR3040"', []),
    WFingerprint('WA501G', 0, 'Basic realm="TP-LINK Wireless AP WA501G"', []),
    WFingerprint('WA5110G', 0, 'Basic realm="TP-LINK Wireless AP WA5110G"', []),
    WFingerprint('WA5210G', 0, 'Basic realm="TP-LINK Wireless AP WA5210G"', []),
    WFingerprint('WA601G', 0, 'Basic realm="TP-LINK Wireless AP WA601G"', []),
    WFingerprint('Archer C5', 0, 'Basic realm="TP-LINK Wireless Dual Band Gigabit Router Archer C5"', []),
    WFingerprint('Archer C7', 0, 'Basic realm="TP-LINK Wireless Dual Band Gigabit Router Archer C7"', []),
    WFingerprint('WDR3600', 0, 'Basic realm="TP-LINK Wireless Dual Band Gigabit Router WDR3600"', []),
    WFingerprint('WDR4300', 0, 'Basic realm="TP-LINK Wireless Dual Band Gigabit Router WDR4300"', []),
    WFingerprint('WDR4900', 0, 'Basic realm="TP-LINK Wireless Dual Band Gigabit Router WDR4900"', []),
    WFingerprint('WDR3500', 0, 'Basic realm="TP-LINK Wireless Dual Band Router WDR3500"', []),
    WFingerprint('WR340G', 0, 'Basic realm="TP-LINK Wireless G Router WR340G"', []),
    WFingerprint('WA730RE', 0, 'Basic realm="TP-LINK Wireless Lite N Access Point WA730RE"', []),
    WFingerprint('WR740N', 0, 'Basic realm="TP-LINK Wireless Lite N Router WR740N"', []),
    WFingerprint('WR740N/WR741ND', 0, 'Basic realm="TP-LINK Wireless Lite N Router WR740N/WR741ND"', []),
    WFingerprint('WR741N', 0, 'Basic realm="TP-LINK Wireless Lite N Router WR741N"', []),
    WFingerprint('WR741ND', 0, 'Basic realm="TP-LINK Wireless Lite N Router WR741ND"', []),
    WFingerprint('WR743ND', 0, 'Basic realm="TP-LINK Wireless Lite N Router WR743ND"', []),
    WFingerprint('MR3420', 0, 'Basic realm="TP-LINK Wireless N 3G Router MR3420"', []),
    WFingerprint('MR3420', 0, 'Basic realm="TP-LINK Wireless N 3G/4G Router MR3420"', []),
    WFingerprint('WA701ND', 0, 'Basic realm="TP-LINK Wireless N Access Point WA701ND"', []),
    WFingerprint('WA801N', 0, 'Basic realm="TP-LINK Wireless N Access Point WA801N"', []),
    WFingerprint('WA901N', 0, 'Basic realm="TP-LINK Wireless N Access Point WA901N"', []),
    WFingerprint('WA901ND', 0, 'Basic realm="TP-LINK Wireless N Access Point WA901ND"', []),
    WFingerprint('WR1042ND', 0, 'Basic realm="TP-LINK Wireless N Gigabit Router WR1042ND"', []),
    WFingerprint('WR1043N', 0, 'Basic realm="TP-LINK Wireless N Gigabit Router WR1043N"', []),
    WFingerprint('WR1043ND', 0, 'Basic realm="TP-LINK Wireless N Gigabit Router WR1043ND"', []),
    WFingerprint('WR1045ND', 0, 'Basic realm="TP-LINK Wireless N Gigabit Router WR1045ND"', []),
    WFingerprint('WR2543ND', 0, 'Basic realm="TP-LINK Wireless N Gigabit Router WR2543ND"', []),
    WFingerprint('WR702N', 0, 'Basic realm="TP-LINK Wireless N Nano Router WR702N"', []),
    WFingerprint('WA830RE', 0, 'Basic realm="TP-LINK Wireless N Range Extender WA830RE"', []),
    WFingerprint('WA840RE', 0, 'Basic realm="TP-LINK Wireless N Router WR840N"', []),
    WFingerprint('WR841N', 0, 'Basic realm="TP-LINK Wireless N Router WR841N"', []),
    WFingerprint('WR843ND', 0, 'Basic realm="TP-LINK Wireless N Router WR843ND"', []),
    WFingerprint('WR940N', 0, 'Basic realm="TP-LINK Wireless N Router WR940N"', []),
    WFingerprint('WR941N', 0, 'Basic realm="TP-LINK Wireless N Router WR941N"', []),
    WFingerprint('WR941ND', 0, 'Basic realm="TP-LINK Wireless N Router WR941ND"', []),
    WFingerprint('WA750RE', 0, 'Basic realm="TP-LINK Wireless Range Extender WA750RE"', []),
    WFingerprint('WA850RE', 0, 'Basic realm="TP-LINK Wireless Range Extender WA850RE"', []),
    WFingerprint('WA860RE', 0, 'Basic realm="TP-LINK Wireless Range Extender WA860RE"', []),
    WFingerprint('WR541G/542G', 0, 'Basic realm="TP-LINK Wireless Router WR541G/542G"', []),
    WFingerprint('WR543G', 0, 'Basic realm="TP-LINK Wireless Router WR543G"', []),
    WFingerprint('WR641G/642G', 0, 'Basic realm="TP-LINK Wireless Router WR641G/642G"', []),
]

# http_fingerprint = namedtuple('h_fp', ['module', 'segment', 'math_type', 'fp', 'extra', 'exploit'])
HTTP_FP = [
    HFingerprint('TL-R470T+', 'SERVER', 0, 'TP-LINK SMB TL-R470T+www_fingerprint(UN), UPnP/1.0', [None, None], []),
    HFingerprint('TL-R480T+', 'SERVER', 0, 'TP-LINK SMB TL-R480T+www_fingerprint(UN), UPnP/1.0', [None, None], []),
    HFingerprint('Range Extender', 'SERVER', 0, 'TP-LINK HTTPD/1.0', [None, None], []),
]

JUMP_LIST = []


class Scanner(BaseScanner):
    prompt = 'TP-LINK Scanner'
    FINGERPRINT_DB = [
        FingerprintConf('TP-LINK', BASIC_FP, HTTP_FP),
    ]

    JUMP_FEATURES = [JUMP_LIST]
