#pylint: disable=unused-variable

from django.test import SimpleTestCase

class SimpleTest(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_aboutpage_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        