
/*!
  * Copyright 2017,  Digital Reasoning
  *
  * Licensed under the Apache License, Version 2.0 (the "License");
  * you may not use this file except in compliance with the License.
  * You may obtain a copy of the License at
  *
  *     http://www.apache.org/licenses/LICENSE-2.0
  *
  * Unless required by applicable law or agreed to in writing, software
  * distributed under the License is distributed on an "AS IS" BASIS,
  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  * See the License for the specific language governing permissions and
  * limitations under the License.
  *
*/

define([
    'jquery',
    'underscore',
    'knockout',
    'bootbox'
], function ($, _, ko, bootbox) {
    'use strict';

    // Define the stack model.
    function Host(raw, parent) {
        var needReload = false;
        if (typeof raw === 'string') {
            raw = parseInt(raw);
        }
        if (typeof raw === 'number') {
            needReload = true;
            // Set the things we need for the reload
            raw = {
                id: raw,
                url: '/api/stacks/' + raw + '/hosts/'
            }
        }

        // Save the raw in order to get things like URLs
        this.raw = raw;

        // Save the parent VM
        this.parent = parent;

        // Save the id
        this.id = raw.id;

        // Editable fields
        this.hostname = ko.observable();
        this.fqdn = ko.observable();
        this.publicDNS = ko.observable();
        this.privateDNS = ko.observable();
        this.hostDefinition = ko.observable();
        this.activity = ko.observable();
        this.health = ko.observable();
        this.labelClass = ko.observable();
        this.healthLabelClass = ko.observable();

        if (needReload) {
            this.reload();
        } else {
            this._process(raw);
        }
    }

    Host.constructor = Host;

    Host.prototype._process = function (raw) {
        this.hostname(raw.hostname);
        this.fqdn(raw.fqdn);
        this.publicDNS(raw.provider_public_dns);
        this.privateDNS(raw.provider_private_dns);
        this.hostDefinition(raw.blueprint_host_definition);
        this.activity(raw.activity);
        this.health(raw.health);

        // Determine what type of label should be around the activity
        switch (raw.activity) {
            case 'idle':
                this.labelClass('label-success');
                break;
            case 'launching':
            case 'provisioning':
            case 'orchestrating':
            case 'resuming':
            case 'pausing':
            case 'executing':
            case 'terminating':
                this.labelClass('label-warning');
                break;
            case 'queued':
            case 'paused':
            case 'terminated':
                this.labelClass('label-info');
                break;
            case 'dead':
                this.labelClass('label-danger');
                break;
            case 'unknown':
            default:
                this.labelClass('label-default');
        }

        // Determine what type of label should be around the health
        switch (raw.health) {
            case 'healthy':
                this.healthLabelClass('label-success');
                break;
            case 'unstable':
                this.healthLabelClass('label-warning');
                break;
            case 'unhealthy':
                this.healthLabelClass('label-danger');
                break;
            case 'unknown':
            default:
                this.healthLabelClass('label-default');
        }
    };

    // Reload the current host
    Host.prototype.reload = function () {
        var self = this;
        return $.ajax({
            method: 'GET',
            url: this.raw.url
        }).done(function (host) {
            self.raw = host;
            self._process(host);
        });
    };

    Host.prototype.delete = function () {
        var self = this;
        bootbox.confirm({
            title: 'Confirm delete of <strong>' + stackTitle + '</strong>',
            message: 'Are you sure you want to delete <strong>' + stackTitle + '</strong>?<br>' +
                     'This will terminate all infrastructure, in addition to ' +
                     'removing all history related to this stack.',
            buttons: {
                confirm: {
                    label: 'Delete',
                    className: 'btn-danger'
                }
            },
            callback: function (result) {
                if (result) {
                    $.ajax({
                        method: 'DELETE',
                        url: self.raw.url
                    }).done(function (stack) {
                        self.raw = stack;
                        self._process(stack);
                    }).fail(function (jqxhr) {
                        var message;
                        try {
                            var resp = JSON.parse(jqxhr.responseText);
                            message = resp.detail.join('<br>');
                        } catch (e) {
                            message = 'Oops... there was a server error.  This has been reported ' +
                                'to your administrators.';
                        }
                        bootbox.alert({
                            title: 'Error deleting stack',
                            message: message
                        });
                    });
                }
            }
        });
    };

    return Host;
});