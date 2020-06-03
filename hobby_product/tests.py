from django.test import TestCase
from .models import hobby_product

# Create your tests here.
class Hobby_ProductTests(TestCase):

    def test_str(self):
        test_name = hobby_product(name='A hobby_product')
        self.assertEqual(str(test_name), 'A hobby_product')