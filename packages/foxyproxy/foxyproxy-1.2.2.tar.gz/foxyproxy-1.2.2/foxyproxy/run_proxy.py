# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
***
Module: foxyproxy - TCP proxy for flexible access to CloudFoxy RESTful API
***

Copyright (C) 2018 Enigma Bridge Limited, registered in the United Kingdom.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
__author__ = "Petr Svenda"
__copyright__ = 'Enigma Bridge Ltd'
__email__ = 'support@enigmabridge.com'
__status__ = 'Development'

from foxyproxy.beacon_thread import BeaconThread
from foxyproxy.proxy_config import ProxyConfig
from foxyproxy.foxyclient import FoxyClient


def proxy_default():
    proxy_cfg = ProxyConfig()   # use default config
    new_beacon = BeaconThread(proxy_cfg)
    FoxyClient.start_server(proxy_cfg, new_beacon)


def proxy_simulated():
    proxy_cfg = ProxyConfig()
    proxy_cfg.test_simulated_card = True
    new_beacon = BeaconThread(proxy_cfg)
    FoxyClient.start_server(proxy_cfg, new_beacon)


def proxy_local():
    proxy_cfg = ProxyConfig()
    proxy_cfg.test_simulated_card = False
    proxy_cfg.test_with_local_reader = True
    # if true, name of local reader will be used instead of supplied remote one
    proxy_cfg.proxy_url = 'http://127.0.0.1:8081'  # rest proxy for simona boards, use basicj for more info
    proxy_cfg.test_local_reader = 'OMNIKEY AG 3121 USB'
    # proxy_cfg.gpprorest_test_local_reader = 'Generic EMV Smartcard Reader 0'

    new_beacon = BeaconThread(proxy_cfg)
    FoxyClient.start_server(proxy_cfg, new_beacon)


def proxy_remote_single_card():
    proxy_cfg = ProxyConfig()
    proxy_cfg.test_simulated_card = False
    proxy_cfg.test_with_local_reader = True
    # if true, name of local reader will be used instead of supplied remote one
    proxy_cfg.proxy_url = 'http://127.0.0.1:8081'  # rest proxy for simona boards, use basicj for more info
    proxy_cfg.test_local_reader = 'OMNIKEY AG 3121 USB'

    new_beacon = BeaconThread(proxy_cfg)
    FoxyClient.start_server(proxy_cfg, new_beacon)


def proxy_remote_simona():
    proxy_cfg = ProxyConfig()
    proxy_cfg.test_simulated_card = False
    proxy_cfg.test_with_local_reader = False
    proxy_cfg.proxy_url = 'http://127.0.0.1:8081'

    new_beacon = BeaconThread(proxy_cfg)
    FoxyClient.start_server(proxy_cfg, new_beacon)


def proxy_remote_mypc():
    proxy_cfg = ProxyConfig()
    proxy_cfg.test_simulated_card = False
    proxy_cfg.test_with_local_reader = True
    proxy_cfg.proxy_url = 'http://192.168.3.129:8081'
    proxy_cfg.test_local_reader = 'OMNIKEY AG Smart Card Reader USB 0'

    new_beacon = BeaconThread(proxy_cfg)
    FoxyClient.start_server(proxy_cfg, new_beacon)


def main():
    # proxy_remote_mypc()
    # proxy_local()
    # proxy_remote_single_card()
    # proxy_simulated()
    proxy_remote_simona()


if __name__ == "__main__":
    main()
