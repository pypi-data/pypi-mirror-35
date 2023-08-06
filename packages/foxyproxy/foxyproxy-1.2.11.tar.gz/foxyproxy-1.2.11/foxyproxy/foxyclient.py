# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
***
Module: foxyproxy - CloudFoxy TCP proxy for flexible access to RESTful API
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

__author__ = "Petr Svenda, Dan Cvrcek"
__copyright__ = 'Enigma Bridge Ltd'
__email__ = 'support@enigmabridge.com'
__status__ = 'Beta'

# Based on Simple socket server using threads by Silver Moon
# (https://www.binarytides.com/python-socket-server-code-example/)
import logging
import coloredlogs
import requests

# noinspection PyProtectedMember

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)
# fh = logging.FileHandler('foxyproxy.log')
# fh.setLevel(logging.INFO)
# logger.addHandler(fh)

coloredlogs.install(level='INFO')
# coloredlogs.install(level='DEBUG', logger=logger) # to suppress logs from libs

logging.basicConfig(level=logging.DEBUG)

class FoxyClient:

    def __init__(self, proxy_conf):
        """

        :type proxy_conf: proxy_config.ProxyConfig
        """
        self.conf = proxy_conf
        pass

    # Function for parsing input request
    # ><reader name>|><cmd ID>:<"APDU" / "RESET" / "ENUM">:<optional hexa string, e.g. "00A4040304">|

    def get_cmd(self, payload):
        return self.get_request(self.conf.proxy_cmd, payload)

    def get_uptime(self):
        return self.get_request(self.conf.proxy_uptime, None)

    def get_inventory(self):
        return self.get_request(self.conf.proxy_inventory, None)

    def get_request(self, cmd, payload):
        response_data = None
        # noinspection PyBroadException
        try:
            logging.debug('Going to to send REST request to GPProREST proxy...')
            r = requests.get(self.conf.proxy_url+cmd, params=payload, headers=self.conf.http_headers)
        except requests.ConnectionError:
            logging.error('Problem with connection - check that the RESTful API host and port are correct %s' %
                          self.conf.proxy_url)
        except Exception:
            logging.error('Problem with connection %s ' % self.conf.proxy_url+cmd)
        else:
            # process response
            logging.debug('Response received: ' + r.content.decode())
            response_data = []
            for line in r.content.decode().splitlines():
                if line != 'null' and len(line) > 0:
                    response_data.append(line)
            r.close()

        return response_data
