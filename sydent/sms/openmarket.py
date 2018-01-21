# -*- coding: utf-8 -*-

# Copyright 2016 OpenMarket Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import random

from base64 import b64encode

from twilio.rest import Client
from twisted.internet import defer, reactor
from sydent.http.httpclient import SimpleHttpClient
from twisted.web.http_headers import Headers

logger = logging.getLogger(__name__)


API_BASE_URL = "https://smsc.openmarket.com/sms/v4/mt"
# The Customer Integration Environment, where you can send
# the same requests but it doesn't actually send any SMS.
# Useful for testing.
#API_BASE_URL = "http://smsc-cie.openmarket.com/sms/v4/mt"

# The TON (ie. Type of Number) codes by type used in our config file
TONS = {
    'long': 1,
    'short': 3,
    'alpha': 5,
}

def tonFromType(t):
    if t in TONS:
        return TONS[t]
    raise Exception("Unknown number type (%s) for originator" % t)


class OpenMarketSMS:
    def __init__(self, sydent):
        self.sydent = sydent
        self.http_cli = SimpleHttpClient(sydent)

    @defer.inlineCallbacks
    def sendTextSMS(self, body, dest, source=None):
        twilio = Client('ACb0db3a1cb0e879877c8c71a04d767d3a', '2d2db813eaabe3f4c2233b5f92c49943')
        twilio.messages.create(to=dest, from_='+15717891325', body=body)
