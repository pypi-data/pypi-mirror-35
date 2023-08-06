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
__author__ = "Dan Cvrcek"
__copyright__ = 'Radical Prime Limited'
__email__ = 'support@radicalprime.com'
__status__ = 'Development'


class RequestData:

    def __init__(self, reader_name, command_id, command_name, command_data=None, command_object=None):
        self.reader_name = reader_name
        self.command_id = command_id
        self.command_name = command_name
        if command_data:
            self.command_data = "".join(command_data.split())  # remove all whitespaces
        else:
            self.command_data = None
        self.command_object = command_object
