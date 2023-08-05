#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import mock

from karborclient.tests.unit import base
from karborclient.tests.unit.v1 import fakes

cs = fakes.FakeClient()
mock_request_return = ({}, {'quota_class': {'plans': 50}})


class QuotaClassesTest(base.TestCaseShell):

    @mock.patch('karborclient.common.http.HTTPClient.json_request')
    def test_quota_class_update(self, mock_request):
        mock_request.return_value = mock_request_return
        cs.quota_classes.update('default', {'plans': 50})
        mock_request.assert_called_with(
            'PUT',
            '/quota_classes/default',
            data={'quota_class': {'plans': 50}}, headers={})

    @mock.patch('karborclient.common.http.HTTPClient.json_request')
    def test_show_quota_class(self, mock_request):
        mock_request.return_value = mock_request_return
        cs.quota_classes.get('default')
        mock_request.assert_called_with(
            'GET',
            '/quota_classes/default',
            headers={})
