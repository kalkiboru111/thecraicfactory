from django.test import TestCase
from .models import Post

# Create your tests here.
class PostTest(TestCase):
    '''
    This defines the tests that posts must pass. These tests will be run against the Post models.
    '''
    def test_unicode(self):
        