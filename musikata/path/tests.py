from django.test import TestCase
from django.test import Client


class UserPathNodeTestCase(TestCase):
    def test_get_userpathnode(self):
        # Should be able to get UserPathNode
        c = Client()
        response = c.get('/path/userpathnode')
        self.assertEquals(response.status_code, 200)
        self.fail("NOT IMPLEMENTED")
