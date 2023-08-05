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

# pylint: disable=wildcard-import, unused-wildcard-import

from __future__ import unicode_literals

from stackdio.server.settings.base import *

# Add additional testing settings here

REST_FRAMEWORK['TEST_REQUEST_DEFAULT_FORMAT'] = 'json'

# Use the plain old db engine for testing so we don't need redis on the server
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
