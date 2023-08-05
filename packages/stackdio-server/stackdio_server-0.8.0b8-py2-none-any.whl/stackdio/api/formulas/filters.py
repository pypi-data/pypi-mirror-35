# -*- coding: utf-8 -*-

# Copyright 2017,  Digital Reasoning
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
#

from __future__ import unicode_literals

import django_filters
from stackdio.api.formulas import models
from stackdio.core.filters import OrFieldsFilter


class FormulaFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_type='icontains')
    q = OrFieldsFilter(field_names=('title', 'description', 'uri', 'root_path'),
                       lookup_type='icontains')

    class Meta:
        model = models.Formula
        fields = (
            'title',
            'uri',
            'root_path',
            'q',
        )
