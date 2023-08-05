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

import logging

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, resolve_url
from django.views.generic import TemplateView
from stackdio.api.cloud.models import CloudAccount

logger = logging.getLogger(__name__)


class StackdioUIView(TemplateView):
    title = 'stackd.io'
    description = 'a modern cloud deployment and provisioning framework for everyone'

    def get_title(self, **kwargs):
        return self.title

    def get_description(self, **kwargs):
        return self.description

    def get_context_data(self, **kwargs):
        context = super(StackdioUIView, self).get_context_data(**kwargs)
        context['title'] = self.get_title(**kwargs)
        context['description'] = self.get_description(**kwargs)
        context['user_agent_only'] = self.request.META.get('ALLOWED_FROM_USER_AGENT', False)
        return context


class RootView(StackdioUIView):
    """
    We don't really have a home page, so let's redirect to either the
    stack or account page depending on certain cases
    """
    def get(self, request, *args, **kwargs):
        has_account_perm = request.user.has_perm('cloud.create_cloudaccount')

        if has_account_perm and CloudAccount.objects.count() == 0:
            # if the user has permission to create an account and there aren't any yet,
            # take them there
            redirect_view = 'ui:cloud-account-list'
        else:
            # Otherwise just go to stacks
            redirect_view = 'ui:stack-list'
        return HttpResponseRedirect(resolve_url(redirect_view))


class AppMainView(StackdioUIView):
    template_name = 'stackdio/js/main.js'
    content_type = 'application/javascript'


class PageView(StackdioUIView):
    viewmodel = None

    def __init__(self, **kwargs):
        super(PageView, self).__init__(**kwargs)
        assert self.viewmodel is not None, (
            'You must specify a viewmodel via the `viewmodel` '
            'attribute of your class.'
        )

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        context['viewmodel'] = self.viewmodel
        return context


class ObjectDetailView(PageView):
    page_id = None
    model = None
    model_verbose_name = None
    model_short_name = None

    lookup_field = 'pk'
    lookup_kwarg = None

    def get_context_data(self, **kwargs):
        context = super(ObjectDetailView, self).get_context_data(**kwargs)

        lookup_kwarg = self.lookup_kwarg or self.lookup_field

        lookup_value = kwargs[lookup_kwarg]
        # Go ahead an raise a 404 here if the account doesn't exist rather
        # than waiting until later.
        obj = get_object_or_404(self.model.objects.all(), **{self.lookup_field: lookup_value})
        context['title'] = '{} - {}'.format(self.model_verbose_name, obj.title)
        context['description'] = obj.description

        model_name = self.model._meta.model_name
        app_label = self.model._meta.app_label

        perm_str = '{}.{{}}_{}'.format(app_label, model_name)

        if not self.request.user.has_perm(perm_str.format('view'), obj):
            # Let the request through if it's allowed via user agent
            if not self.request.META.get('ALLOWED_FROM_USER_AGENT', False):
                raise Http404()
        context[self.model_short_name] = obj
        context['has_admin'] = self.request.user.has_perm(perm_str.format('admin'), obj)
        context['has_delete'] = self.request.user.has_perm(perm_str.format('delete'), obj)
        context['has_update'] = self.request.user.has_perm(perm_str.format('update'), obj)
        context['page_id'] = self.page_id
        return context


class ModelPermissionsView(PageView):
    template_name = 'stackdio/permissions.html'
    model = None

    def __init__(self, **kwargs):
        super(ModelPermissionsView, self).__init__(**kwargs)
        assert self.model is not None, (
            'You must specify a model via the `model` '
            'attribute of your class.'
        )

    def get_context_data(self, **kwargs):
        context = super(ModelPermissionsView, self).get_context_data(**kwargs)
        model_name = self.model._meta.model_name
        context['object_type'] = model_name.capitalize()
        return context

    def get(self, request, *args, **kwargs):
        app_label = self.model._meta.app_label
        model_name = self.model._meta.model_name
        if not request.user.has_perm('%s.admin_%s' % (app_label, model_name)):
            # No permission granted
            raise Http404()
        return super(ModelPermissionsView, self).get(request, *args, **kwargs)


class ObjectPermissionsView(PageView):
    template_name = 'stackdio/permissions.html'

    def get_object(self):
        raise NotImplementedError()

    def get_context_data(self, **kwargs):
        context = super(ObjectPermissionsView, self).get_context_data(**kwargs)
        context['object_type'] = self.get_object()._meta.model_name.capitalize()
        context['object_id'] = kwargs.get('pk')
        return context

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        app_label = obj._meta.app_label
        model_name = obj._meta.model_name
        # Check permissions on the object
        if not request.user.has_perm('%s.admin_%s' % (app_label, model_name), obj):
            # No permission granted
            raise Http404()
        return super(ObjectPermissionsView, self).get(request, *args, **kwargs)
