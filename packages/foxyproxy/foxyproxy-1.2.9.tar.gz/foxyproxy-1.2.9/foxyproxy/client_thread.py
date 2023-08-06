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
import binascii
import logging
import threading
import time

from foxyproxy.beacon_thread import BeaconThread
from foxyproxy.foxyclient import FoxyClient, InputRequestData
from foxyproxy.foxyclient import logger
from foxyproxy.foxyclient import CMD_APDU, CMD_CHAIN, CMD_READER_NOT_FOUND, CMD_VAGUE_NAME, CMD_ALIAS, \
    CMD_ENUM, CMD_SIGN, CMD_SEPARATOR, CMD_RESPONSE_END, CMD_READER_WRONG_DATA, CMD_READER_WRONG_PIN, CMD_RESET, \
    CMD_RESPONSE_FAIL

__author__ = "Dan Cvrcek"
__copyright__ = 'Radical Prime Limited'
__email__ = 'support@radicalprime.com'
__status__ = 'Development'


class ClientThread(threading.Thread):
    """
    Function for handling connections. This will be used to create threads
    """
    def __init__(self, connection, ip, port, proxy_cfg, beacon):
        """

        :type proxy_cfg: proxy_config.ProxyConfig
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