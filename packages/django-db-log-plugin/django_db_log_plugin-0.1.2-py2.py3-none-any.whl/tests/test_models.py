#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django_db_log
------------

Tests for `django_db_log` models module.
"""

from django.test import TestCase

from django_db_log import models
import logging

logger = logging.getLogger(__name__)


class TestLogging(TestCase):

    def test_logger(self):
        logger.error('Logger test')

