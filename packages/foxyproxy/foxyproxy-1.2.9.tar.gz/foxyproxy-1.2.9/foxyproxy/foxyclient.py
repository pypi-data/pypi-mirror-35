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
from client_thread import ClientThread

__author__ = "Petr Svenda, Dan Cvrcek"
__copyright__ = 'Enigma Bridge Ltd'
__email__ = 'support@enigmabridge.com'
__status__ = 'Beta'

# Based on Simple socket server using threads by Silver Moon
# (https://www.binarytides.com/python-socket-server-code-example/)
import logging
import coloredlogs
import requests
import socket
import sys

# noinspection PyProtectedMember

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# fh = logging.FileHandler('foxyproxy.log')
# fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# logger.addHandler(fh)
logger.addHandler(ch)

coloredlogs.install(level='INFO')
# coloredlogs.install(level='DEBUG', logger=logger) # to suppress logs from libs

logging.basicConfig(level=logging.DEBUG)

PROXY_SERVER_PORT = 4001
CLOUD_FOXY_HOST = 'http://localhost:8081'

CMD_APDU = "APDU"
CMD_RESET = "RESET"  # requests smartcard reset
CMD_SIGN = "SIGN"  # requests eIDAS signature
CMD_CHAIN = "CHAIN"  # requests certificate chain from a given smart card
CMD_ALIAS = "ALIASES"  # requests all names from certificates
CMD_ENUM = "ENUM"  # requests a list of readers
CMD_SEPARATOR = ":"
CMD_LINE_SEPARATOR = "|"
CMD_RESPONSE_END = "\n@@"
CMD_RESPONSE_FAIL = "C081"
CMD_VAGUE_NAME = "C082"
CMD_READER_NOT_FOUND = "C083"
CMD_READER_WRONG_DATA = "C084"
CMD_READER_WRONG_PIN = "C085"


class InputRequestData:

    def __init__(self, reader_name, command_id, command_name, command_data=None, command_object=None):
        self.reader_name = reader_name
        self.command_id = command_id
        self.command_name = command_name
        if command_data:
            self.command_data = "".join(command_data.split())  # remove all whitespaces
        else:
            self.command_data = None
        self.command_object = command_object


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

    @staticmethod
    def start_server(proxy_cfg, beacon):
        # we start one monitoring thread, while the main thread will start spawning TCP server threads
        # when the monitoring thread detects restart of the RESTful server, it will load all certificates from connected
        # smart-cards, these are needed for requests coming from jsignpdf - SIGN - where responses consist of
        # a list of certificates and a result of signing.

        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.debug('Socket created')

        bound = False
        tries = 10
        while tries > 0 and not bound:
            try:
                soc.bind((proxy_cfg.socket_host, proxy_cfg.socket_port))
                logging.debug(
                    'Socket bind complete. host:{0}, port:{1}'.format(proxy_cfg.socket_host, proxy_cfg.socket_port))
                bound = True
            except socket.error as msg:
                logging.error('Bind failed. Error Code : %s' % str(msg))
            tries -= 1

        if not bound:
            logging.error("The port is used by another process")
            sys.exit()

        # Start listening on socket
        soc.listen(10)
        logging.info('Socket now listening')

        # now keep talking with the client
        while True:
            # wait to accept a connection - blocking call
            conn, addr = soc.accept()
            ip, port = str(addr[0]), str(addr[1])
            logging.info('Connected with ' + ip + ':' + port)

            # start new thread takes with arguments
            new_client = ClientThread(conn, ip, port, proxy_cfg, beacon)

            new_client.start()
            new_client.join()

        # soc.close()  #  unreachable
