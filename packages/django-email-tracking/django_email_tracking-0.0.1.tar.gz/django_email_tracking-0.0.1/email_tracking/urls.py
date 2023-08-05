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

from django.conf.urls import url

from email_tracking.views import email_tracking_receiver

app_name = "email_tracking"

urlpatterns = [
  url(
    r"^((?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?).png$",
    email_tracking_receiver,
    name="receiver"
  ),
]
