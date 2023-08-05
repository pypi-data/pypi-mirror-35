#!/usr/bin/env python
# vi: et sw=2 fileencoding=utf-8

#============================================================================
# Email Tracking
# Copyright (c) 2018 Pispalan Insinööritoimisto Oy (http://www.pispalanit.fi)
#
# All rights reserved.
# Redistributions of files must retain the above copyright notice.
#
# @description [File description]
# @created     11.01.2018
# @author      Harry Karvonen <harry.karvonen@pispalanit.fi>
# @copyright   Copyright (c) Pispalan Insinööritoimisto Oy
# @license     All rights reserved
#============================================================================

from __future__ import unicode_literals

import django.dispatch


s_email_tracking_received = django.dispatch.Signal(
  providing_args=[
    "email_tracking_id",
    "email_tracking_type",
  ],
)
