#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) Smart Arcs Ltd, Enigma Bridge Ltd, registered in the United Kingdom.
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Dan Cvrcek <support@smartarchitects.co.uk>, August 2018

__copyright__ = "Smart Arcs Ltd, Enigma Bridge Ltd"
__email__ = "support@smartarchitects.co.uk"
__status__ = "Beta"

# from foxyproxy.foxyclient import FoxyClient
# from foxyproxy.beacon_thread import BeaconThread
# from foxyproxy.foxyclient import InputRequestData

# from foxyproxy.foxyclient import *

try:
    import pkg_resources
    pkg_resources.declare_namespace(__name__)
except ImportError:
    import pkgutil

    # noinspection PyUnboundLocalVariable
    __path__ = pkgutil.extend_path(__path__, __name__)
