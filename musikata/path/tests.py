import json
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from .models import PathNode, UserPathNode


class UserPathTestCase(TestCase):

    def setUp(self):
        # Setup path.
        path_nodes = [
            PathNode(path_id='testPath', xpath='/'),
            PathNode(path_id='testPath', xpath='/A'),
            PathNode(path_id='testPath', xpath='/B'),
            PathNode(path_id='someOtherPath', xpath='/'),
        ]
        for path_node in path_nodes: path_node.save()

        # Setup user path.
        user = User.objects.create_user('louis', 'louis@satchmo.com', 'horn')
        user_path_nodes = [
            UserPathNode(user=user, path_node=path_nodes[1],
                         status='completed'),
            UserPathNode(user=user, path_node=path_nodes[3],
                         status='completed'),
        ]
        for user_path_node in user_path_nodes: user_path_node.save()

    def test_user_path_endpoint(self):
        """ Should return data object containing path/userPath node data."""
        expected_data = {
            'path_nodes': [
                {'path_id': 'testPath', 'xpath': '/'},
                {'path_id': 'testPath', 'xpath': '/A'},
                {'path_id': 'testPath', 'xpath': '/B'},
            ],
            'user_path_nodes': [
                {'path_id': 'testPath', 'xpath': '/A', 'status': 'completed'},
            ]
        }

        response = Client().get('/path/userpath/testPath/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode())
        self.assertEqual(data, expected_data)


class PathNodeTestCase(TestCase):
    def test_create_path_node(self):
        path_node = PathNode.objects.create()
        self.assertIsNotNone(path_node.id)

class UserPathNodeTestCase(TestCase):
    def test_create_user_path_node(self):
        user = User.objects.create_user('louis', 'louis@satchmo.com', 'horn')
        path_node = PathNode.objects.create()
        user_path_node = UserPathNode.objects.create(user=user,
                                                     path_node=path_node)
        self.assertIsNotNone(user_path_node.id)

    def test_update_user_path_node(self):
        # Create node in db.
        user = User.objects.create_user('louis', 'louis@satchmo.com', 'horn')
        path_node = PathNode.objects.create(path_id='testPath', xpath='/A')
        UserPathNode.objects.create(user=user, path_node=path_node)

        # post data.
        post_url = '/path/userpathnode/{}/{}/'.format(user.id, path_node.id)
        response = Client().post(post_url, {'status': 'completed'})

        # Check response.
        self.assertEqual(response.status_code, 200)

        # Check that node was updated.
        updated_user_path_node = UserPathNode.objects.filter(
            user__id=user.id).filter(path_node__id=path_node.id).first()
        self.assertEqual(updated_user_path_node.status, 'completed')

    def xtest_create_user_path_node(self):
        # Post data.
        # check that node was created.
        pass


    def xtest_get_userpathnode(self):
        # Should be able to get UserPathNode
        c = Client()
        response = c.get('/path/userpathnode')
        self.assertEquals(response.status_code, 200)
        self.fail("NOT IMPLEMENTED")
