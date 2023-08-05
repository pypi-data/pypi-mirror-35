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

import base64
import json

from django.http import Http404, HttpResponse
from django.core.urlresolvers import reverse

from email_tracking.signals import s_email_tracking_received


pixel_1x1_base64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGP6zwAAAgcBApocMXEAAAAASUVORK5CYII="


def email_tracking_receiver(request, b64data):
  " GET ../b64data/ return 1x1 pixel"
  if request.method != "GET":
    raise Http404()

  try:
    data = json.loads(base64.b64decode(b64data))
  except ValueError:
    raise Http404()

  s_email_tracking_received.send_robust(dict,
    email_tracking_id=data.get("email_tracking_id"),
    email_tracking_type=data.get("email_tracking_type"),
  )

  return HttpResponse(
    base64.b64decode(
      pixel_1x1_base64,
    ), # transparent white 1x1 pixel
    content_type="image/png",
  )
  # def email_tracking_receiver
