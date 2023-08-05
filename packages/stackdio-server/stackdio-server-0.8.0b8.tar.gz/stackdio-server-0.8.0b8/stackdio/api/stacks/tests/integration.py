# -*- coding: utf-8 -*-

# Copyright 2017,  Digital Reasoning
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import unicode_literals

# class StackTestCase(StackdioTestCase, PermissionsMixin):
#     """
#     Tests for CloudAccount things
#     """
#
#     permission_tests = {
#         'model': models.Stack,
#         'create_data': {
#             'bluprint': 1,
#             'title': 'test',
#             'description': 'test',
#             'namespace': 'test',
#         },
#         'endpoint': '/api/stacks/{0}/',
#         'permission': 'stacks.%s_stack',
#         'permission_types': [
#             {
#                 'perm': 'view', 'method': 'get'
#             },
#             {
#                 'perm': 'update', 'method': 'patch', 'data': {'title': 'test2'}
#             },
#             {
#                 'perm': 'delete', 'method': 'delete', 'code': status.HTTP_204_NO_CONTENT
#             },
#         ]
#     }
#
#     @classmethod
#     def setUpTestData(cls):
#         super(StackdioTestCase, cls).setUpTestData()
