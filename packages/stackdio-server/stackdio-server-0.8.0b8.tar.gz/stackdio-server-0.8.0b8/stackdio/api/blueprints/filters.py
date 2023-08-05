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
from stackdio.api.blueprints import models
from stackdio.core.filters import OrFieldsFilter, LabelFilterMixin


class BlueprintFilter(django_filters.FilterSet, LabelFilterMixin):
    title = django_filters.CharFilter(lookup_type='icontains')
    label = django_filters.MethodFilter(action='filter_label')
    q = OrFieldsFilter(field_names=('title', 'description'),
                       lookup_type='icontains',
                       include_labels=True)

    class Meta:
        model = models.Blueprint
        fields = (
            'title',
            'label',
            'q',
        )
