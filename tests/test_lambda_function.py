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

import json
import unittest
import urllib
from lambda_function import lambda_handler

sample_uri = 'https://raw.githubusercontent.com/alexa/alexa-smarthome/master/sample_messages/'


class TestLambdaFunction(unittest.TestCase):

    @staticmethod
    def get_sample(url):
        content = urllib.request.urlopen(url).read().decode("utf-8")
        return json.loads(content)

    def test_authorization(self):
        r = self.get_sample(sample_uri + 'Authorization/Authorization.AcceptGrant.request.json')
        c = None
        response = lambda_handler(request=r, context=c)
        # print(json.dumps(response, indent=2))
        self.assertEqual(response['event']['header']['namespace'], 'Alexa.Authorization')
        self.assertEqual(response['event']['header']['name'], 'AcceptGrant.Response')

    def test_discovery(self):
        r = self.get_sample(sample_uri + 'Discovery/Discovery.request.json')
        c = None
        response = lambda_handler(request=r, context=c)
        # print(json.dumps(response, indent=2))
        self.assertEqual(response['event']['header']['namespace'], 'Alexa.Discovery')
        self.assertEqual(response['event']['header']['name'], 'Discover.Response')

    def test_powercontroller_off(self):
        r = self.get_sample(sample_uri + 'PowerController/PowerController.TurnOff.request.json')
        c = None
        response = lambda_handler(request=r, context=c)
        # print(json.dumps(response, indent=2))
        self.assertEqual(response['event']['header']['namespace'], 'Alexa')
        self.assertEqual(response['event']['header']['name'], 'Response')


if __name__ == '__main__':
    unittest.main()
