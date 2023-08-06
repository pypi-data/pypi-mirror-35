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
import base64
import binascii
import datetime
import logging
import threading
import time

from cryptography import x509
from cryptography.hazmat.backends import default_backend
# noinspection PyProtectedMember
from cryptography.x509 import ExtensionOID

import foxyproxy

__author__ = "Dan Cvrcek"
__copyright__ = 'Radical Prime Limited'
__email__ = 'support@radicalprime.com'
__status__ = 'Development'


# noinspection PyUnusedLocal
class BeaconThread(threading.Thread):
    """
    Class starts a thread, which regularly connects to a restful server and re-builds a dictionary of certificates
    when the server restarts
    """

    def __init__(self, proxy_cfg):
        """

        :type proxy_cfg: proxy_config.ProxyConfig
        """
        threading.Thread.__init__(self)
        self.server = proxy_cfg
        self.last_timer = 0
        self.certificates = {}  # this is a hash table we need to initialize now
        self.cert_names = []  # this will contain a mapping from names to smartcard readers {name:<>, reader:<>}
        self.card_cas = {}
        self.proxy_cfg = proxy_cfg
        self.enigma = foxyproxy.FoxyClient(proxy_cfg)

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
                if len(response_all) < 1 or response_all[0][-4:] != "9000":
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
                        subject_cn = ""
                        for attribute in cert.subject:
                            oid_in = attribute.oid
                            # dot = oid_in.dotted_string
                            # noinspection PyProtectedMember
                            oid_name = oid_in._name
                            val = attribute.value
                            subject_list.append('%s: %s' % (oid_name, val))
                            if oid_name.lower() == "commonname":
                                subject_cn = val
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
                            logging.debug("New CA certificate from reader %s: %s" % (reader, subject_cn))
                            # this is a CA, we store it in card CA list
                            self.card_cas[reader].append({
                                'name': subject,
                                'issuer': issuer,
                                'cert': base64.standard_b64encode(binascii.a2b_hex(new_cert))
                            })
                        else:
                            logging.info("New user certificate from reader %s: %s" % (reader, subject_cn))
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
                    'file_id': 0})
                # we will try to find it with the first signature ...  end_cert_id})
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
