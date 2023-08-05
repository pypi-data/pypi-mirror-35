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


class Settings:
  from django.conf import settings as __settings
  __defaults = {}


  def __init__(self, **kwargs):
    self.__defaults = kwargs
    # def __init__


  def __getattr__(self, name):
    try:
      return getattr(self.__settings, name)
    except AttributeError as e:
      try:
        return self.__defaults[name]
      except KeyError:
        raise e
    # def __getattr__


  # class Settings

settings = Settings(
  EMAIL_TRACKING_BACKEND='django.core.mail.backends.smtp.EmailBackend',
  EMAIL_TRACKING_BASE_URL="https://example.com",
)
