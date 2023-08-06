# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
***
Module: foxyproxy - CloudFoxy proxy - TCP proxy for flexible access to CloudFoxy RESTful API
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
import sys
import getopt

__author__ = "Petr Svenda, Dan Cvrcek"
__copyright__ = 'Enigma Bridge Ltd'
__email__ = 'support@enigmabridge.com'
__status__ = 'Beta'

from foxyclient import FoxyClient
from foxyproxy import BeaconThread
from foxyproxy.proxy_config import ProxyConfig


def print_help():
    print("The proxy accepts the following parameters:")
    print("  -h -  this help")
    print("  -p<port> - port where the proxy listens")
    print("  -s<url:port> - address of the CloudFoxy RESTful API, e.g., http://server.cloudfoxy.com:8081")


def main():
    custom_port = None
    custom_server = None
    if len(sys.argv) > 1:
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hp:s:")
        except getopt.GetoptError:
            # print help information and exit:
            print_help()
            sys.exit(2)

        for o, a in opts:
            if o == '-h':
                print_help()
            else:
                if o == '-p':
                    if a.isdigit():
                        custom_port = int(a)
                if o == '-s':
                    custom_server = a.strip()

    proxy_cfg = ProxyConfig()   # use default config
    if custom_port:
        proxy_cfg.socket_port = custom_port
    if custom_server:
        proxy_cfg.proxy_url = custom_server

    print("The proxy will listen on port %d and connect to RESTful server at %s" %
          (proxy_cfg.socket_port, proxy_cfg.proxy_url))

    new_beacon = BeaconThread(proxy_cfg)
    new_beacon.start()
    FoxyClient.start_server(proxy_cfg, new_beacon)


if __name__ == '__main__':
    main()
