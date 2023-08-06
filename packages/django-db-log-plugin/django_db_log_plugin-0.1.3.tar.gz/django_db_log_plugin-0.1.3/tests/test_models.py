#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django_db_log
------------

Tests for `django_db_log` models module.
"""

from django.test import TestCase


from model_mommy import mommy
from django_db_log.models import GeneralLog, InfoLog, DebugLog, ErrorLog

import logging

logger = logging.getLogger(__name__)


class GeneralLogging(TestCase):

    def setUp(self):
        self.general_log = mommy.make(GeneralLog)

    def test_create_general_log(self):
        title = '{0} - {1}'.format(self.general_log.time, self.general_log.message[:100])
        self.assertTrue(isinstance(self.general_log, GeneralLog))
        self.assertEqual(self.general_log.__unicode__(), title)


class InfoLogging(TestCase):

    def setUp(self):
        self.info_log = mommy.make(InfoLog)

    def test_create_info_log(self):
        title = '{0} - {1}'.format(self.info_log.time, self.info_log.message[:100])
        self.assertTrue(isinstance(self.info_log, InfoLog))
        self.assertEqual(self.info_log.__unicode__(), title)


class DebugLogging(TestCase):

    def setUp(self):
        self.debug_log = mommy.make(DebugLog)

    def test_create_debug_log(self):
        title = '{0} - {1}'.format(self.debug_log.time, self.debug_log.message[:100])
        self.assertTrue(isinstance(self.debug_log, DebugLog))
        self.assertEqual(self.debug_log.__unicode__(), title)


class ErrorLogging(TestCase):

    def setUp(self):
        self.error_log = mommy.make(ErrorLog)

    def test_create_error_log(self):
        title = '{0} - {1}'.format(self.error_log.time, self.error_log.message[:100])
        self.assertTrue(isinstance(self.error_log, ErrorLog))
        self.assertEqual(self.error_log.__unicode__(), title)

