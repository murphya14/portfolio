# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

class Hobby_ProductTests(TestCase):

    def test_str(self):
        test_name = hobby_product(name='A hobby_product')
        self.assertEqual(str(test_name), 'A hobby_product')
