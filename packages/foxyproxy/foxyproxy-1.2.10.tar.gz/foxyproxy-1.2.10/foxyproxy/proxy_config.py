#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
***
Module:
***

 Copyright (C) Radical Prime Limited, registered in the United Kingdom.
 This file is owned exclusively by Radical Prime Limited.
 Unauthorized copying of this file, via any medium is strictly prohibited
 Proprietary and confidential
 Written by Dan Cvrcek <support@radicalprime.com>, May 2018
"""
from foxyproxy.foxyclient import PROXY_SERVER_PORT, CLOUD_FOXY_HOST

__author__ = "Dan Cvrcek"
__copyright__ = 'Radical Prime Limited'
__email__ = 'support@radicalprime.com'
__status__ = 'Development'


class ProxyConfig:

    def __init__(self):
        self.test_simulated_card = False  # if true, completely simulated response is send back

        self.socket_host = ''    # Symbolic name meaning all available interfaces
        self.socket_port = PROXY_SERVER_PORT  # Arbitrary non-privileged port

        self.test_simulated_card = False
        self.proxy_url = CLOUD_FOXY_HOST
        #  rest proxy for CloudFoxy hardware platform, use basicj for more info
        self.proxy_cmd = '/api/v1/basic'
        self.proxy_uptime = '/api/v1/hello'
        self.proxy_inventory = '/api/v1/inventory'
        self.test_local_reader = None
        # self.test_local_reader = 'OMNIKEY AG 3121 USB'
        # self.test_local_reader = 'Generic EMV Smartcard Reader 0'

        self.http_headers = {'X-Auth-Token': 'b'}

        self.test_with_local_reader = True
        # if true, name of local reader will be used instead of supplied remote one
