from django.test import TestCase


# Create your tests here.

class Test(TestCase):
    def test_success(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)
