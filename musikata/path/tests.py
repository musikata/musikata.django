from django.test import TestCase
from django.test import Client
from .models import PathNode, UserPathNode
from django.contrib.auth.models import User


class PathNodeTestCase(TestCase):
    def test_create_path_node(self):
        path_node = PathNode.objects.create()
        self.assertIsNotNone(path_node.id)

class UserPathNodeTestCase(TestCase):
    def test_create_user_path_node(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com',
                                        'johnpassword')
        path_node = PathNode.objects.create()
        user_path_node = UserPathNode.objects.create(user=user,
                                                     path_node=path_node)
        self.assertIsNotNone(user_path_node.id)

    def xtest_get_userpathnode(self):
        # Should be able to get UserPathNode
        c = Client()
        response = c.get('/path/userpathnode')
        self.assertEquals(response.status_code, 200)
        self.fail("NOT IMPLEMENTED")
