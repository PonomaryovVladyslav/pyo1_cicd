from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.

class Test(TestCase):
    def test_success(self):
        self.assertTrue(True)

    def test_fail_fixed(self):
        self.assertTrue(True)

    def test_user(self):
        User.objects.create_user(username='test', password='test')
        self.assertEqual(User.objects.count(), 1)
