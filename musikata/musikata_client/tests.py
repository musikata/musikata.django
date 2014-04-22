from django.test import TestCase, Client


class MusikataClientTestCase(TestCase):
    def test_client_view(self):
        response = Client().get('/client/')
        self.assertEqual(response.status_code, 200)
