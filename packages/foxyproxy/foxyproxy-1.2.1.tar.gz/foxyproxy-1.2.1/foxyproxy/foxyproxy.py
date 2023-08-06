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
import base64
import datetime
import logging
import coloredlogs
import requests
import socket
import sys
import time
import threading
import binascii
from cryptography import x509
from cryptography.hazmat.backends import default_backend
# noinspection PyProtectedMember
from cryptography.x509 import ExtensionOID

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


class BeaconThread(threading.Thread):
    """
    Class starts a thread, which regularly connects to a restful server and re-builds a dictionary of certificates
    when the server restarts
    """

    def __init__(self, proxy_cfg):
        """

        :type proxy_cfg: ProxyConfig
        """
        threading.Thread.__init__(self)
        self.server = proxy_cfg
        self.last_timer = 0
        self.certificates = {}  # this is a hash table we need to initialize now
        self.cert_names = []  # this will contain a mapping from names to smartcard readers {name:<>, reader:<>}
        self.card_cas = {}
        self.proxy_cfg = proxy_cfg
        self.enigma = FoxyClient(proxy_cfg)

        response_data = self.enigma.get_uptime()

        # let's parse the response, which is of 3 lines
        if response_data is None:
            logging.error("Hello request returns incorrect data None")
            exit()
        elif len(response_data) < 3:
            logging.error("Hello request returns incorrect data %s " % '|'.join(response_data))
            exit()

        # let's take the second string on 2nd line, convert to integer
        self.last_timer = int(response_data[1].split()[1])

        # here we read out all the certificates so we can send them out
        self.read_certificates()
        pass

    def get_reader(self, subject):
        """
        Accepts names of certificate owners and returns a list of readers that have certs with this string in cert names
        :param subject: a substring of a name from a certificate
        :return:
        """
        reader = []
        for one_name in self.cert_names:
            if subject in one_name['name']:
                reader.append(one_name)

        return reader

    def update_file_id(self, reader, file_id):
        """
        If we find a correct file_id for the user's private key, we set it in the cert_names list
        :param reader: a copy of one of the items retrieved from cert_names
        :param file_id: an integer - the new file_id
        :return: None
        """
        new_cert_names = []
        for one_name in self.cert_names:
            if reader['name'] == one_name['name']:
                one_name['file_id'] = file_id
            new_cert_names.append(one_name)
        self.cert_names = new_cert_names

    @staticmethod
    def encode_cf_reader(name):
        """
        Adds decoration to CloudFoxy reader names
        :type name: str
        """
        if name[0] == '/' and name.find('@') > 1:
            name = "CloudFoxy net " + name[1:]  # also remove the '/' at the beginning
            name = name.replace('@', '-')
        else:
            name = "CloudFoxy usb " + name
        return name

    @staticmethod
    def decode_cf_reader(name):
        """
        Removes a decoration from CloudFoxy reader names.
        :type name: str
        """
        prefix_net = "CloudFoxy net"
        prefix_usb = "CloudFoxy usb"
        name = name.strip()
        if name.find(prefix_net) == 0:  # network name - strip prefix, add '/' and replace '-' with '@'
            name = '/' + name[len(prefix_net):]
            name = name.replace('-', '@')
        elif name.find(prefix_usb) == 0:  # local/usb name - strip prefix only
            name = name[len(prefix_usb):]
        return name

    def get_all_readers(self):
        """
        No parameters, returns a list of readers
        :return:
        """
        readers = []
        for one_name in self.cert_names:
            name = BeaconThread.encode_cf_reader(one_name['reader'])
            readers.append(base64.b64encode(name.encode('utf-8')).decode('ascii'))

        return readers

    def get_aliases(self):
        """
        Extracts names from cerificates and returns them as a list
        :return:
        """
        all_names = []
        for each_name in self.cert_names:
            all_names.append(base64.b64encode(each_name['name'].encode('utf-8')).decode('ascii'))
        return all_names

    def get_certs(self, reader_id):
        """

        :param reader_id: e.g., /192.168.42.10@1
        :return:
        """
        str_certs = ""
        if reader_id in self.certificates.keys():
            str_certs += self.certificates.get(reader_id)['cert'].decode('ascii')
            for ca_cert in self.certificates.get(reader_id)['chain']:
                str_certs += ":" + ca_cert['cert'].decode('ascii')

        return str_certs

    def run(self):

        while True:
            # noinspection PyBroadException
            try:
                time.sleep(10)  # every this many seconds, we will check up-time
                response_data = self.enigma.get_uptime()

                # let's parse the response, which is of 3 lines
                if len(response_data) < 3:
                    logging.error("Hello request returns incorrect data %s " % '|'.join(response_data))
                    exit()

                new_uptime = int(
                    response_data[1].split()[1])  # let's take the second string on 2nd line, convert to integer

                if new_uptime < self.last_timer:
                    # rest all structures, read card certificates from scratch
                    self.certificates = {}  # this is a hash table we need to initialize now
                    # this will contain a mapping from names to smartcard readers {name:<>, reader:<>}
                    self.cert_names = []
                    self.card_cas = {}
                    self.read_certificates()

                # we always set the new timer value
                self.last_timer = new_uptime
                pass  # end of the infinite cycle loop
            except Exception:
                # we ignore exceptions, keep running
                pass
        pass

    def read_certificates(self):

        # let's now get a list of card readers and ATRs
        response_data = self.enigma.get_inventory()

        for each_line in response_data:
            logging.info("Found a new chip %s" % each_line)
            items = each_line.split()
            if items[1].strip().upper() == "3BF81300008131FE454A434F5076323431B7":
                # we found an expected EIDAS smart-card
                self.certificates[items[0]] = {}  # we need to get the certificates

        # now, let's query smart cards
        # 1. we select folder with certificates
        #    A4 02 0C 02 56 30
        #    and request all items
        #    00 B2 xx 04 00/FF   // where xx goes from 1, till we get and error "6A 83"
        #    we parse each response 01 xx (if length < 0x82) ...
        #       01 xx ..... 02 04 ... 10 04 ff ff aa aa -> FOLDER/FILE .... 12 04 00 ll ll -> ll ll = cert length
        # 2. we load the certificate
        #    00 A4 00 0C 02 3F 00
        #    00 A4 01 0C 02 3F 50
        #    00 A4 01 0C 02 ff ff
        #    00 A4 01 0C 02 aa aa
        #    and read the cert with 00 B0 xx 00 00, where xx = 0 ... x
        # 3. we parse certificates - find user certs and their chains
        # 4. store in a hash map
        for reader in self.certificates.keys():

            ##########################
            # a new approach to derive the file ID for the private key
            ##########################
            payload = {'apdu': '00A4000C023F00', 'terminal': reader, 'reset': 0}
            response_all = self.enigma.get_cmd(payload)
            payload = {'apdu': '00A4010C023F50', 'terminal': reader, 'reset': 0}
            response_all = self.enigma.get_cmd(payload)
            payload = {'apdu': '00A4010C023F10', 'terminal': reader, 'reset': 0}
            response_all = self.enigma.get_cmd(payload)
            payload = {'apdu': '00A4020C025660', 'terminal': reader, 'reset': 0}
            response_all = self.enigma.get_cmd(payload)

            cert_file_id = 1
            not_found = True
            while not_found:
                payload = {'apdu': '00B2%02X0400' % cert_file_id, 'terminal': reader}  # a folder
                response_all = self.enigma.get_cmd(payload)
                # print(response_all[0])
                if response_all[0][-4:] != "9000":
                    cert_file_id -= 1  # the previous one was the last good
                    not_found = False
                else:
                    cert_file_id += 1

            ##########################
            ##########################

            latest_cert_time = 0
            self.card_cas[reader] = []
            payload = {'apdu': '00A40004023F0000', 'terminal': reader, 'reset': 1}
            self.enigma.get_cmd(payload)

            new_item = True
            certificate_id = 1
            end_subject = ""
            end_issuer = ""
            end_cert_id = 0

            # payload = {'apdu': '00A4000C023F00', 'terminal': reader}  # switch to the app
            # response_all = self.enigma.get_cmd(payload)
            # if response_all[0][-4:] != "9000":
            #     continue  # with the next reader
            # payload = {'apdu': '00A4010C023F50', 'terminal': reader}  # select files with objects
            # response_all = self.enigma.get_cmd(payload)
            # if response_all[0][-4:] != "9000":
            #     continue  # with the next reader
            # payload = {'apdu': '00A4020C025620', 'terminal': reader}  # a folder
            # response_all = self.enigma.get_cmd(payload)
            # if response_all[0][-4:] != "9000":
            #     continue  # with the next reader
            # not_found = True
            # while not_found:
            #     payload = {'apdu': '00B2%02X0400' % cert_file_id, 'terminal': reader}  # a folder
            #     response_all = self.enigma.get_cmd(payload)
            #     if response_all[0][-4:] != "9000":
            #         logging.error("We didn't find a file descriptor for signing")
            #         break
            #     elif response_all[0][2:6] == "0100":
            #         not_found = False
            #         cert_file_id = bytearray.fromhex(response_all[0][:2])[0]  # this should contain the file ID
            #         logging.info("We found private key file descriptor %d for %s" % (cert_file_id, reader))
            #     else:
            #         cert_file_id += 1

            while new_item:
                payload = {'apdu': '00A4000C023F00', 'terminal': reader}  # switch to the app
                self.enigma.get_cmd(payload)
                payload = {'apdu': '00A4010C023F50', 'terminal': reader}  # select files with objects
                self.enigma.get_cmd(payload)
                payload = {'apdu': '00A4010C023F10', 'terminal': reader}  # we need a directory structure
                self.enigma.get_cmd(payload)
                payload = {'apdu': "00A4020C025630", 'terminal': reader}  # and a list of certificates
                response_all = self.enigma.get_cmd(payload)
                if response_all[0][-4:] != "9000":
                    logging.error("00A4020C025630 command returned an error (reader %s) - %s" %
                                  (reader, response_all[0][-4:]))
                    break

                # select 1..n-th certificate record
                payload = {'apdu': "00B2%02X0400" % certificate_id, 'terminal': reader}
                certificate_id += 1
                response_all = self.enigma.get_cmd(payload)
                if len(response_all) < 1:
                    logging.error("00B2%02X0400 command didn't return any response" % certificate_id)
                    break
                if response_all[0][-4:] != "9000":
                    logging.info("00B2%02X0400 command returned an error - %s" %
                                  (certificate_id, response_all[0][-4:]))
                    break
                # keep the first line without the last 4 characters
                raw_response = bytearray.fromhex(response_all[0][:-4])  # remove the first ASN.1 tag
                if raw_response[1] <= 0x81:
                    raw_response = raw_response[2:]  # ... and its length
                else:
                    offset = (raw_response[1] - 128) + 2  # ... and its length, we only keep the value
                    raw_response = raw_response[offset:]  # the long length encoding 01 82 xx xx
                file_id = None
                cert_len = 0
                while (len(raw_response) > 2) and ((file_id is None) or (cert_len == 0)):
                    if raw_response[0] == 0x10:  # this is 2 file descriptors to select a certificate
                        file_id = raw_response[2:6]
                    if raw_response[0] == 0x12:  # this is the length of the certificate we expect
                        cert_len = ((raw_response[2]*256 + raw_response[3])*256 + raw_response[4])*256 + raw_response[5]
                    raw_response = raw_response[(2+raw_response[1]):]
                # let's get a certificate now - first select one
                payload = {'apdu': '00A4000C023F00', 'terminal': reader}
                self.enigma.get_cmd(payload)
                payload = {'apdu': "00A4010C023F50", 'terminal': reader}
                self.enigma.get_cmd(payload)
                apdu_value = "00A4010C02%s" % binascii.b2a_hex(file_id[0:2]).decode('ascii')  # select cert folder /3f20
                payload = {'apdu': apdu_value, 'terminal': reader}
                self.enigma.get_cmd(payload)
                apdu_value = "00 a4 020C02%s" % binascii.b2a_hex(file_id[2:4]).decode('ascii')  # and the cert we want
                payload = {'apdu': apdu_value, 'terminal': reader}
                response_all = self.enigma.get_cmd(payload)
                if len(response_all) > 0 and response_all[0][-4:] == '9000':
                    counter = 0
                    new_cert = ""
                    while cert_len > 0:  # reading the cert - multiple APDUs
                        payload = {'apdu': "00B0%02X0000" % counter, 'terminal': reader}
                        response_all = self.enigma.get_cmd(payload)
                        if len(response_all) < 1 or response_all[0][-4:] != "9000":
                            break
                        new_cert += response_all[0][:-4]
                        cert_len -= (len(response_all[0])/2 - 2)
                        counter += 1

                    if cert_len <= 0:  # it should end up in cert_len == 0
                        # we got a cert
                        cert = x509.load_der_x509_certificate(binascii.a2b_hex(new_cert), default_backend())
                        subject_list = []
                        subject_CN = ""
                        for attribute in cert.subject:
                            oid_in = attribute.oid
                            # dot = oid_in.dotted_string
                            # noinspection PyProtectedMember
                            oid_name = oid_in._name
                            val = attribute.value
                            subject_list.append('%s: %s' % (oid_name, val))
                            if oid_name.lower() == "commonname":
                                subject_CN = val
                        subject_list.sort()
                        subject = ', '.join(subject_list)
                        issuer_list = []
                        for attribute in cert.issuer:
                            oid_in = attribute.oid
                            # dot = oid_in.dotted_string
                            # noinspection PyProtectedMember
                            oid_name = oid_in._name
                            val = attribute.value
                            issuer_list.append('%s: %s' % (oid_name, val))
                        issuer_list.sort()
                        issuer = ', '.join(issuer_list)
                        ext = cert.extensions.get_extension_for_oid(ExtensionOID.BASIC_CONSTRAINTS)
                        if ext and ext.value and ext.value.ca:
                            logging.debug("New CA certificate from reader %s: %s" % (reader, subject_CN))
                            # this is a CA, we store it in card CA list
                            self.card_cas[reader].append({
                                'name': subject,
                                'issuer': issuer,
                                'cert': base64.standard_b64encode(binascii.a2b_hex(new_cert))
                            })
                        else:
                            logging.info("New user certificate from reader %s: %s" % (reader, subject_CN))
                            # it's an end-user certificate
                            issued_at = BeaconThread.unix_time(cert.not_valid_before)
                            if issued_at > latest_cert_time:
                                self.certificates[reader]['cert'] = \
                                    base64.standard_b64encode(binascii.a2b_hex(new_cert))
                                end_issuer = issuer
                                end_subject = subject
                                end_cert_id = cert_file_id
                            else:
                                # we will only take the latest certificate - if there are more end-user certs
                                pass
                    else:
                        logging.error("Error reading a certificate from smart card, selector: %s" % apdu_value)

                else:
                    # cert file selection returned error
                    if len(response_all) > 0:
                        logging.error("Certificate file selection returned error: %s" % response_all[0])
                    else:
                        logging.error("Certificate file selection returned no response")

            # this is the end of reading certificates from smart card - we now need to create a chain
            # and extract the subject from the end-user cert
            if end_subject == "" or end_issuer == "":
                logging.error("No end-user certificate found on this smart card %s" % reader)
            else:
                # create a link from name to smart card
                self.cert_names.append({
                    'name': end_subject,
                    'reader': reader,
                    'pin': None,
                    'file_id': 0})  #  we will try to find it with the first signature ...  end_cert_id})
                # let's create a chain
                root = False
                chain = []
                while not root:
                    next_found = False
                    for ca_cert in self.card_cas[reader]:
                        if ca_cert['name'] == end_issuer:
                            next_found = True
                            chain.append(ca_cert)
                            end_issuer = ca_cert['issuer']
                            if ca_cert['name'] == ca_cert['issuer']:
                                root = True
                            break
                    if not next_found:
                        break
                if len(chain) < 1:
                    logging.error("No certificate found for %s" % end_subject)
                else:
                    self.certificates[reader]['chain'] = chain

        pass

    @staticmethod
    def unix_time(dt):
        if dt is None:
            return None
        cur = datetime.datetime.utcfromtimestamp(0)
        if dt.tzinfo is not None:
            cur.replace(tzinfo=dt.tzinfo)
        else:
            cur.replace(tzinfo=None)
        # noinspection PyBroadException
        try:
            return (dt - cur).total_seconds()
        except Exception:
            pass


class ClientThread(threading.Thread):
    """
    Function for handling connections. This will be used to create threads
    """
    def __init__(self, connection, ip, port, proxy_cfg, beacon):
        """

        :type proxy_cfg: ProxyConfig
        """
        threading.Thread.__init__(self)
        self.connection = connection
        self.ip = ip
        self.port = port
        self.proxy_cfg = proxy_cfg
        self.beacon = beacon

    def run(self):
        try:
            # infinite loop so that function do not terminate and thread do not end.
            while True:
                # Receiving from client
                reader = None
                password = None
                commands = []
                # first we read all the commands
                data_raw = self.connection.recv(4096)
                if len(data_raw) == 0:  # connection was closed
                    break
                buffer_list = []
                try:
                    buffer_list.append(data_raw)
                except TypeError:
                    logging.error("Received data can't be converted to text")
                    pass

                data = ''.join(buffer_list)
                data = data.decode('utf-8')

                # data = ">Simona /111.222.123.033@07|\n>2:RESET|\n>3:APDU:1100000000|\n>4:APDU:2200000000|" \
                #        "\n>5:APDU:3300000000|"
                # data = ">K|\n>3:SIGN:0000000000000000000000000000000000000000|"
                lines = data.splitlines()
                for line in lines:
                    line = line.strip()  # remove white space - beginning & end
                    if line[0] == '#':
                        # this may be in internal info
                        pass
                    elif line[0] != '>':
                        # we will ignore this line
                        continue
                    line = line[1:].strip()  # ignore the '>' and strip whitespaces
                    if line.rfind('|') < 0:
                        logging.info("Possibly missing | at the end of the line %s " % line)
                    else:
                        line = line[:line.rfind(u"|")]
                    if not reader:
                        cmd_parts = line.split(u':')
                        reader = cmd_parts[0]  # if '|' is not in string, it will take the whole line
                        if len(cmd_parts) > 1:
                            password = cmd_parts[1]
                    else:
                        cmd_parts = line.split(':')
                        if len(cmd_parts) < 2 or len(cmd_parts) > 4:
                            logging.error('Invalid line %s - ignoring it' % line)
                            continue

                        item = {'id': cmd_parts[0], 'name': cmd_parts[1], 'bytes': None, 'object': None}
                        if len(cmd_parts) > 2:
                            item['bytes'] = cmd_parts[2]
                        if len(cmd_parts) > 3:
                            item['object'] = cmd_parts[3]
                        commands.append(item)

                if len(commands) == 0:
                    logging.error("No commands to process")
                    time.sleep(0.1)  # sleep little before making another receive attempt
                    continue

                for command in commands:
                    input_req = InputRequestData(reader,
                                                 command['id'], command['name'], command['bytes'], command['object'])

                    logging.info(u"Reader:'{0}',CommandID:'{1}',Command:'{2}'".format(
                        input_req.reader_name,
                        input_req.command_id,
                        input_req.command_name))

                    # for testing with local card, rename CloudFoxy readers to local one
                    if self.proxy_cfg.test_with_local_reader:
                        if input_req.reader_name == BeaconThread.decode_cf_reader(input_req.reader_name):
                            if self.proxy_cfg.test_local_reader is not None:
                                input_req.reader_name = self.proxy_cfg.test_local_reader
                                logging.debug(u'Changing remote reader {0} to local reader {1} for testing'
                                              .format(input_req.reader_name, self.proxy_cfg.test_local_reader))

                    processing_command = input_req.command_name.upper()
                    enigma_client = FoxyClient(self.proxy_cfg)
                    # SEND APDU
                    if processing_command == CMD_APDU:
                        if self.proxy_cfg.test_simulated_card:
                            response_data = "102030409000"
                        else:
                            payload = {'apdu': input_req.command_data, 'terminal': input_req.reader_name}
                            response_all = enigma_client.get_cmd(payload)
                            if len(response_all) > 0:
                                response_data = response_all[0]
                            else:
                                response_data = "C090"
                    elif processing_command == CMD_CHAIN:
                        reader = self.beacon.get_reader(input_req.reader_name)
                        if len(reader) != 1:
                            if len(reader) == 0:
                                # we haven't found the name
                                response_data = CMD_READER_NOT_FOUND
                            else:
                                # the name is not unique
                                response_data = CMD_VAGUE_NAME
                        else:
                            # and we need to get the certificate chain
                            response_data = self.beacon.get_certs(reader[0]['reader'])

                    elif processing_command == CMD_ALIAS:
                        aliases = self.beacon.get_aliases()
                        response_data = "|".join(aliases)

                    elif processing_command == CMD_ENUM:
                        readers = self.beacon.get_all_readers()
                        response_data = "|".join(readers)

                    elif processing_command == CMD_SIGN:
                        # signing consists of the following APDUs
                        # apdu=00A4000C023F00\&reset=1  - card reset
                        # apdu=00A4010C020604           - select of the PIN file
                        # apdu=002000810733323837313935  - PIN check  - 3287295
                        # apdu=00 22 41 AA 04 89 02 14 30   . 41 - MSE:SET, AA - hash,
                        #                      89021430 = sha-256, 89021410 = sha-1
                        # apdu=00 22 41 B6 0A 84(SDO ref) 03 800400 8903 13 23 30 -
                        #                      8903132330 - rsa-sha-256, 8903132310 = rsa-sha1
                        # apdu=00 2A 90 A0 22 90 20 D0 6C EF 8B 4A DA 05 75 9E 1A 2C 75 23 64 15 08 DC BA 5C B6 E7 C3
                        # 3F E8 A2 C6 43 C0 1B C4 CE 34

                        reader = self.beacon.get_reader(input_req.reader_name)
                        if len(reader) != 1:
                            if len(reader) == 0:
                                # we haven't found the name
                                response_data = CMD_READER_NOT_FOUND
                            else:
                                # the name is not unique
                                response_data = CMD_VAGUE_NAME

                            response = ">{0}{1}{2}{3}\n".format(input_req.command_id, CMD_SEPARATOR, response_data,
                                                                CMD_RESPONSE_END)
                            logging.info(response)
                            self.connection.sendall(response.encode("utf-8"))
                            exit()

                        # we have a reader, let's do the signing
                        sha_id = None
                        if len(input_req.command_data) == 40:
                            sha_id = "10"
                        elif len(input_req.command_data) == 64:
                            sha_id = "30"
                        else:
                            response_data = CMD_READER_WRONG_DATA

                            response = ">{0}{1}{2}{3}\n".format(input_req.command_id, CMD_SEPARATOR, response_data,
                                                                CMD_RESPONSE_END)
                            logging.info(response)
                            self.connection.sendall(response.encode("utf-8"))
                            exit()

                        payload = {'reset': '1', 'terminal': reader[0]['reader'], 'apdu': '00A4000C023F00'}
                        enigma_client.get_cmd(payload)
                        payload = {'terminal': reader[0]['reader'], 'apdu': '00A4010C020604'}
                        response_all = enigma_client.get_cmd(payload)
                        # PIN
                        # if the password is set
                        pin_ok = True
                        if password is not None:
                            encoded_password = binascii.b2a_hex(password.encode('ascii')).decode('ascii')  # 3287195
                            if (reader[0]['pin'] is not None) and (reader[0]['pin'] == encoded_password):
                                logger.error("Blocked repeated use of incorrect PIN to reader %s, remaining tries %s"
                                             % (reader[0]['reader'], response_all[-1:]))
                                pin_ok = False
                            else:
                                payload = {'terminal': reader[0]['reader'],
                                           'apdu': '00200081%02X%s' % (len(password), encoded_password)
                                           }
                                response_all = enigma_client.get_cmd(payload)
                                if (response_all is not None) and (len(response_all) > 0) \
                                        and response_all[0][-4:-1] == "63C":
                                    # there is a problem with PIN - the counter was decreased
                                    logger.error("Incorrect PIN to reader %s, remaining tries %s" %
                                                 (reader[0]['reader'], response_all[0][-1:]))
                                    reader[0]['pin'] = encoded_password
                                elif (response_all is not None) and (len(response_all) > 0) \
                                        and response_all[0][-4:] == "9000":
                                    reader[0]['pin'] = None
                                elif (response_all is None) or len(response_all) < 1:
                                    logger.error("Error with PIN verification at reader %s - no details available" %
                                                 reader[0]['reader'])
                                    pin_ok = False
                                else:
                                    logger.error("Error with PIN verification at reader %s, the error code is %s" %
                                                 (reader[0]['reader'], response[0]))
                                    pin_ok = False
                        if not pin_ok:
                            response_data = CMD_READER_WRONG_PIN
                        else:
                            # let's do signing - we may try a few times if 'file_id' is not set
                            keep_trying = True
                            temp_file_id = reader[0]['file_id']

                            key_id_limit = 15
                            if temp_file_id == 0:
                                temp_file_id = key_id_limit
                            while keep_trying:
                                # h MSE:Set sha-256
                                payload = {'terminal': reader[0]['reader'], 'apdu': '002241AA04890214%s'
                                                                                    % sha_id}
                                enigma_client.get_cmd(payload)
                                # h MSE:Set DST
                                payload = {'terminal': reader[0]['reader'], 'apdu': '002241B60A 840380%02X00 89031323%s'
                                                                                    % (temp_file_id, sha_id)}
                                response_all = enigma_client.get_cmd(payload)
                                if (response_all is not None) and (len(response_all) > 0) \
                                        and (response_all[0][-4:] != "9000" or len(response_all[0]) < 4):
                                    logging.error("Error setting MSE DST reader %s - code: %s" %
                                                  (reader[0]['reader'], response_all[0]))

                                # send the hash to the card
                                sha_length = int(len(input_req.command_data) / 2)
                                payload = {'terminal': reader[0]['reader'], 'apdu': '002a90a0%02X90%02X%s' %
                                                                                    (sha_length+2,
                                                                                     sha_length,
                                                                                     input_req.command_data)
                                           }
                                response_all = enigma_client.get_cmd(payload)
                                if (response_all is not None) and (len(response_all) > 0) \
                                        and (response_all[0][-4:] != "9000" or len(response_all[0]) < 4):
                                    logging.error("Error sending hash for signing reader %s - code %s" %
                                                  (reader[0]['reader'], response_all[0]))

                                # finally, request signing and collect the signature
                                payload = {'terminal': reader[0]['reader'], 'apdu': "002A9E9A00"}
                                response_all = enigma_client.get_cmd(payload)
                                if response_all[0][-4:] != "9000":
                                    response_data = ""
                                    logging.error("Signing unsuccessful reader %s, error code %s" %
                                                  (reader[0]['reader'], response_all[0][-4:]))
                                    response_data = response_all[0][-4:]
                                    # let's see if we should try again
                                    if reader[0]['file_id'] == 0 and key_id_limit > 0:
                                        key_id_limit -= 1
                                        temp_file_id -= 1
                                    else:
                                        keep_trying = False
                                else:
                                    if reader[0]['file_id'] == 0:
                                        self.beacon.update_file_id(reader[0], temp_file_id)
                                    response_data = response_all[0][0:-4]
                                    keep_trying = False
                        pass
                    elif processing_command == CMD_RESET:  # RESET
                        if self.proxy_cfg.test_simulated_card:
                            # test response, send to SIMONA instead
                            response_data = "621A82013883023F008404524F4F5485030079AD8A0105A1038B01019000"
                        else:
                            payload = {'reset': '1', 'terminal': input_req.reader_name}
                            response_all = enigma_client.get_cmd(payload)
                            if len(response_all) > 0:
                                response_data = response_all[0]
                            else:
                                response_data = "C090"

                    else:  # No valid command found
                        response_data = CMD_RESPONSE_FAIL

                    response = ">{0}{1}{2}{3}\n".format(input_req.command_id, CMD_SEPARATOR, response_data,
                                                        CMD_RESPONSE_END)
                    logging.info(response)
                    self.connection.sendall(response.encode("utf-8"))
                # break  # we close the connection after
        except Exception as ex:
            logging.info('Exception in serving response, ending thread %s' % ex)
            logging.info('\n')

        # Terminate connection for given client (if outside loop)
        self.connection.close()
        return


class FoxyClient:

    def __init__(self, proxy_conf):
        """

        :type proxy_conf: ProxyConfig
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
