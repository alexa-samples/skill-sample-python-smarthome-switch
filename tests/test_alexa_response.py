# -*- coding: utf-8 -*-

# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Amazon Software License (the "License"). You may not use this file except in
# compliance with the License. A copy of the License is located at
#
#    http://aws.amazon.com/asl/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import unittest
from alexa.skills.smarthome import AlexaResponse


class TestAlexaResponse(unittest.TestCase):

    def test_response(self):
        response = AlexaResponse().get()
        
        self.assertEqual(response['event']['header']['namespace'], 'Alexa')
        self.assertEqual(response['event']['header']['name'], 'Response')

    def test_response_cookie(self):
        response = AlexaResponse(cookie={"key": "value"}).get()
        
        self.assertEqual(response['event']['endpoint']['cookie']['key'], 'value')

    def test_response_error(self):
        payload_error = {"type": "INVALID_SOMETHING", "message": "ERROR_MESSAGE"}
        response = AlexaResponse(name="ErrorResponse", payload=payload_error).get()
        
        self.assertEqual(response['event']['header']['name'], 'ErrorResponse')

    def test_discovery(self):
        adr = AlexaResponse(namespace="Alexa.Discovery", name="Discover.Response")
        capability_alexa = adr.create_payload_endpoint_capability()
        capability_alexa_powercontroller = adr.create_payload_endpoint_capability(
            interface="Alexa.PowerController",
            supported=[{"name": "powerState"}])
        adr.add_payload_endpoint(capabilities=[capability_alexa, capability_alexa_powercontroller])
        response = adr.get()

        self.assertEqual(response['event']['header']['namespace'], 'Alexa.Discovery')
        self.assertEqual(response['event']['header']['name'], 'Discover.Response')
        self.assertEqual(response['event']['payload']['endpoints'][0]['friendlyName'], 'Sample Endpoint')
        self.assertEqual(response['event']['payload']['endpoints'][0]['capabilities'][0]['type'], 'AlexaInterface')


if __name__ == '__main__':
    unittest.main()
