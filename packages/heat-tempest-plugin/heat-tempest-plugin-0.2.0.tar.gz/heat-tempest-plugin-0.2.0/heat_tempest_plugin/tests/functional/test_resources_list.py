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

from tempest.lib import decorators

from heat_tempest_plugin.tests.functional import functional_base


test_template_depend = {
    'heat_template_version': '2013-05-23',
    'resources': {
        'test1': {
            'type': 'OS::Heat::TestResource',
            'properties': {
                'value': 'Test1',
            }
        },
        'test2': {
            'type': 'OS::Heat::TestResource',
            'depends_on': ['test1'],
            'properties': {
                'value': 'Test2',
            }
        }
    }
}


class ResourcesList(functional_base.FunctionalTestsBase):

    @decorators.idempotent_id('b65b5c82-68b0-42c9-82a0-c0e74e9ad906')
    def test_filtering_with_depend(self):
        stack_identifier = self.stack_create(template=test_template_depend)
        [test2] = self.client.resources.list(stack_identifier,
                                             filters={'name': 'test2'})

        self.assertEqual('CREATE_COMPLETE', test2.resource_status)

    @decorators.idempotent_id('97a65d53-b449-4a43-8283-42d43b165756')
    def test_required_by(self):
        stack_identifier = self.stack_create(template=test_template_depend)
        [test1] = self.client.resources.list(stack_identifier,
                                             filters={'name': 'test1'})

        self.assertEqual(['test2'], test1.required_by)
