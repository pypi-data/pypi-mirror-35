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

import datetime
import os
import subprocess

VERSION = (0, 8, 0, 'b', 8)


def get_version(version):
    """
    Returns a PEP 440-compliant version number from VERSION.

    Created by modifying django.utils.version.get_version
    """

    # Now build the two parts of the version number:
    # major = X.Y[.Z]
    # sub = .devN - for development releases
    #     | {a|b|rc}N - for alpha, beta and rc releases
    #     | .postN - for post-release releases

    assert len(version) == 5

    # Build the first part of the version
    major = '.'.join(str(x) for x in version[:3])

    # Just return it if this is a final release version
    if version[3] == 'final':
        return major

    # Add the rest
    sub = ''.join(str(x) for x in version[3:5])

    if version[3] == 'dev':
        # Override the sub part.  Add in a timestamp
        timestamp = get_git_changeset()
        sub = 'dev%s' % (timestamp if timestamp else '')
        return '%s.%s' % (major, sub)
    if version[3] == 'post':
        # We need a dot for post
        return '%s.%s' % (major, sub)
    elif version[3] in ('a', 'b', 'rc'):
        # No dot for these
        return '%s%s' % (major, sub)
    else:
        raise ValueError('Invalid version: %s' % str(version))


# Borrowed directly from django
def get_git_changeset():
    """Returns a numeric identifier of the latest git changeset.

    The result is the UTC timestamp of the changeset in YYYYMMDDHHMMSS format.
    This value isn't guaranteed to be unique, but collisions are very unlikely,
    so it's sufficient for generating the development version numbers.
    """
    repo_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    git_log = subprocess.Popen('git log --pretty=format:%ct --quiet -1 HEAD',
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               shell=True, cwd=repo_dir, universal_newlines=True)
    timestamp = git_log.communicate()[0]
    try:
        timestamp = datetime.datetime.utcfromtimestamp(int(timestamp))
    except ValueError:
        # If we can't get the timestamp, get the current UTC time
        timestamp = datetime.datetime.utcnow()
    return timestamp.strftime('%Y%m%d%H%M%S')


__version__ = get_version(VERSION)
