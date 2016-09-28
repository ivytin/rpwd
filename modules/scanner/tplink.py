#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'

from template.scanner import www_fingerprint, http_fingerprint

# www_fingerprint = namedtuple('w_fp', ['module', 'match_type', 'fp', 'exploit'])
BASIC_FP = [
    www_fingerprint('R860', 0, 'Basic realm="TP-LINK Router R860"', []),
    www_fingerprint('WR720N', 0, 'Basic realm="150Mbps Wireless N Router TL-WR720N"', []),
    www_fingerprint('TD-8840T 2.0', 0, 'Basic realm="TD-8840T 2.0"', []),
    www_fingerprint('TD-8840T', 0, 'Basic realm="TD-8840T"', []),
    www_fingerprint('TL-WR841HP', 0, 'Basic realm="TP-LINK 300Mbps High Power Wireless N Router TL-WR841HP"', []),
    www_fingerprint('TD-VG3631', 0, 'Basic realm="TP-LINK 300Mbps Wireless N VoIP ADSL2+ Modem Router TD-VG3631"', []),
    www_fingerprint('Archer C5', 0, 'Basic realm="TP-LINK AC1200 Wireless Dual Band Gigabit Router Archer C5"', []),
    www_fingerprint('Archer C8', 0, 'Basic realm="TP-LINK AC1750 Wireless Dual Band Gigabit Router Archer C8"', []),
    www_fingerprint('Archer C9', 0, 'Basic realm="TP-LINK AC1750 Wireless Dual Band Gigabit Router Archer C9"', []),
    www_fingerprint('TD-8840T', 0, 'Basic realm="TP-LINK ADSL2+ Modem Router TD-8840T"', []),
    www_fingerprint('R600VPN', 0, 'Basic realm="TP-LINK Gigabit Broadband VPN Router R600VPN"', []),
    www_fingerprint('WR842ND', 0, 'Basic realm="TP-LINK Multi-Function Wireless N Router WR842ND"', []),
    www_fingerprint('WA7210N', 0, 'Basic realm="TP-LINK Outdoor Wireless Access Point WA7210N"', []),
    www_fingerprint('MR3020', 0, 'Basic realm="TP-LINK Portable Wireless N 3G/4G Router MR3020"', []),
    www_fingerprint('MR3040', 0, 'Basic realm="TP-LINK Portable Wireless N 3G/4G Router MR3040"', []),
    www_fingerprint('WA501G', 0, 'Basic realm="TP-LINK Wireless AP WA501G"', []),
    www_fingerprint('WA5110G', 0, 'Basic realm="TP-LINK Wireless AP WA5110G"', []),
    www_fingerprint('WA5210G', 0, 'Basic realm="TP-LINK Wireless AP WA5210G"', []),
    www_fingerprint('WA601G', 0, 'Basic realm="TP-LINK Wireless AP WA601G"', []),
    www_fingerprint('Archer C5', 0, 'Basic realm="TP-LINK Wireless Dual Band Gigabit Router Archer C5"', []),
    www_fingerprint('Archer C7', 0, 'Basic realm="TP-LINK Wireless Dual Band Gigabit Router Archer C7"', []),
    www_fingerprint('WDR3600', 0, 'Basic realm="TP-LINK Wireless Dual Band Gigabit Router WDR3600"', []),
    www_fingerprint('WDR4300', 0, 'Basic realm="TP-LINK Wireless Dual Band Gigabit Router WDR4300"', []),
    www_fingerprint('WDR4900', 0, 'Basic realm="TP-LINK Wireless Dual Band Gigabit Router WDR4900"', []),
    www_fingerprint('WDR3500', 0, 'Basic realm="TP-LINK Wireless Dual Band Router WDR3500"', []),
    www_fingerprint('WR340G', 0, 'Basic realm="TP-LINK Wireless G Router WR340G"', []),
    www_fingerprint('WA730RE', 0, 'Basic realm="TP-LINK Wireless Lite N Access Point WA730RE"', []),
    www_fingerprint('WR740N', 0, 'Basic realm="TP-LINK Wireless Lite N Router WR740N"', []),
    www_fingerprint('WR740N/WR741ND', 0, 'Basic realm="TP-LINK Wireless Lite N Router WR740N/WR741ND"', []),
    www_fingerprint('WR741N', 0, 'Basic realm="TP-LINK Wireless Lite N Router WR741N"', []),
    www_fingerprint('WR741ND', 0, 'Basic realm="TP-LINK Wireless Lite N Router WR741ND"', []),
    www_fingerprint('WR743ND', 0, 'Basic realm="TP-LINK Wireless Lite N Router WR743ND"', []),
    www_fingerprint('MR3420', 0, 'Basic realm="TP-LINK Wireless N 3G Router MR3420"', []),
    www_fingerprint('MR3420', 0, 'Basic realm="TP-LINK Wireless N 3G/4G Router MR3420"', []),
    www_fingerprint('WA701ND', 0, 'Basic realm="TP-LINK Wireless N Access Point WA701ND"', []),
    www_fingerprint('WA801N', 0, 'Basic realm="TP-LINK Wireless N Access Point WA801N"', []),
    www_fingerprint('WA901N', 0, 'Basic realm="TP-LINK Wireless N Access Point WA901N"', []),
    www_fingerprint('WA901ND', 0, 'Basic realm="TP-LINK Wireless N Access Point WA901ND"', []),
    www_fingerprint('WR1042ND', 0, 'Basic realm="TP-LINK Wireless N Gigabit Router WR1042ND"', []),
    www_fingerprint('WR1043N', 0, 'Basic realm="TP-LINK Wireless N Gigabit Router WR1043N"', []),
    www_fingerprint('WR1043ND', 0, 'Basic realm="TP-LINK Wireless N Gigabit Router WR1043ND"', []),
    www_fingerprint('WR1045ND', 0, 'Basic realm="TP-LINK Wireless N Gigabit Router WR1045ND"', []),
    www_fingerprint('WR2543ND', 0, 'Basic realm="TP-LINK Wireless N Gigabit Router WR2543ND"', []),
    www_fingerprint('WR702N', 0, 'Basic realm="TP-LINK Wireless N Nano Router WR702N"', []),
    www_fingerprint('WA830RE', 0, 'Basic realm="TP-LINK Wireless N Range Extender WA830RE"', []),
    www_fingerprint('WA840RE', 0, 'Basic realm="TP-LINK Wireless N Router WR840N"', []),
    www_fingerprint('WR841N', 0, 'Basic realm="TP-LINK Wireless N Router WR841N"', []),
    www_fingerprint('WR843ND', 0, 'Basic realm="TP-LINK Wireless N Router WR843ND"', []),
    www_fingerprint('WR940N', 0, 'Basic realm="TP-LINK Wireless N Router WR940N"', []),
    www_fingerprint('WR941N', 0, 'Basic realm="TP-LINK Wireless N Router WR941N"', []),
    www_fingerprint('WR941ND', 0, 'Basic realm="TP-LINK Wireless N Router WR941ND"', []),
    www_fingerprint('WA750RE', 0, 'Basic realm="TP-LINK Wireless Range Extender WA750RE"', []),
    www_fingerprint('WA850RE', 0, 'Basic realm="TP-LINK Wireless Range Extender WA850RE"', []),
    www_fingerprint('WA860RE', 0, 'Basic realm="TP-LINK Wireless Range Extender WA860RE"', []),
    www_fingerprint('WR541G/542G', 0, 'Basic realm="TP-LINK Wireless Router WR541G/542G"', []),
    www_fingerprint('WR543G', 0, 'Basic realm="TP-LINK Wireless Router WR543G"', []),
    www_fingerprint('WR641G/642G', 0, 'Basic realm="TP-LINK Wireless Router WR641G/642G"', []),
]

# http_fingerprint = namedtuple('h_fp', ['module', 'segment', 'math_type', 'fp', 'extra', 'exploit'])
HTTP_FP = [
    http_fingerprint('TL-R470T+', 'SERVER', 0, 'TP-LINK SMB TL-R470T+www_fingerprint(UN), UPnP/1.0', [], []),
    http_fingerprint('TL-R480T+', 'SERVER', 0, 'TP-LINK SMB TL-R480T+www_fingerprint(UN), UPnP/1.0', [], []),
    http_fingerprint('Range Extender', 'SERVER', 0, 'TP-LINK HTTPD/1.0', [], []),
]

JUMP_LIST = []
