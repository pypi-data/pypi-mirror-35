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

import threading
import base64
import json

from lxml.html import fromstring, tostring
from lxml.html import builder as E

from django.core.mail import get_connection
from django.core.mail.backends.base import BaseEmailBackend
from django.core.urlresolvers import reverse

from email_tracking.conf import settings


class EmailBackendWrapper(BaseEmailBackend):
  """
  Email backend wrapper that will wraps backend configured in
  settings.EMAIL_TRACKING_BACKEND

source: https://github.com/IndustriaTech/django-email-tracker/blob/master/email_tracker/backends.py
  """

  def __init__(self, **kwargs):
    super(EmailBackendWrapper, self).__init__(**kwargs)
    self.connection = get_connection(settings.EMAIL_TRACKING_BACKEND, **kwargs)
    self._lock = threading.RLock()

  def open(self):
    return self.connection.open()

  def close(self):
    return self.connection.close()

  def send_messages(self, email_messages):
    if not email_messages:
      return

    with self._lock:
      new_conn_created = self.open()
      num_sent = 0
      for message in email_messages:
        sent = self._send(message)
        if sent:
          num_sent += 1
        if new_conn_created:
          self.close()

    return num_sent
    # def send_messages

  def _send(self, message):
    return self.connection.send_messages([message])

  # def EmailBackendWrapper


class EmailTrackingBackend(EmailBackendWrapper):


  def _send(self, message):
    self.add_tracking(message)
    return super(EmailTrackingBackend, self)._send(message)


  def add_tracking(self, message):
    """message.extra_headers
    EmailTrackingID, pakollinen
    EmailTrackingType, vapaaehtoinen
    """
    # tracking pixel base64(json({"email_tracking_id": 1, "email_tracking_type": None}))
    if "EmailTrackingID" not in message.extra_headers:
      return

    data = {
      "email_tracking_id": message.extra_headers.pop("EmailTrackingID"),
    }

    if "EmailTrackingType" in message.extra_headers:
      data["email_tracking_type"] = message.extra_headers.pop("EmailTrackingType")

    if message.content_subtype == "plain":
      message.body = "<html><body><pre>%s</pre></body></html>" % (
        message.body,
      )
      message.content_subtype = "html"


    b64data = base64.b64encode(json.dumps(data))
    tracking_url = settings.EMAIL_TRACKING_BASE_URL + reverse(
      "email_tracking:receiver", args=(b64data,),
    )

    html_doc = fromstring(message.body)
    html_body = html_doc.find("body")

    if html_body is None:
      html_body = html_doc

    html_body.insert(0, E.IMG("", src=tracking_url))

    message.body = tostring(html_doc)
    # def add_tracking


  # class EmailTrackingBackend
