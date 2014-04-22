import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import PathNode, UserPathNode
from .serializers import UserPathNodeSerializer


def get_userpath(request, path_id):
    # Fetch related PathNode & UserPathNodes.
    path_nodes = PathNode.objects.filter(path_id=path_id).order_by('xpath')
    user_path_nodes = UserPathNode.objects.filter(
        path_node__path_id=path_id).order_by('path_node__xpath')

    # Serialize path nodes.
    def serialize_path_node(path_node):
        serialized = {}
        for field in ['path_id', 'xpath']:
            serialized[field] = getattr(path_node, field, None)
        return serialized
    serialized_path_nodes = list(map(serialize_path_node, path_nodes))

    # Serialize user path nodes.
    def serialize_user_path_node(user_path_node):
        serialized = {}
        serialized.update(serialize_path_node(
            user_path_node.path_node))
        serialized['status'] = user_path_node.status
        return serialized
    serialized_user_path_nodes = list(map(serialize_user_path_node,
                                          user_path_nodes))

    return HttpResponse(json.dumps({
        'path_nodes': serialized_path_nodes,
        'user_path_nodes': serialized_user_path_nodes
    }))

def get_userpathnode(request):
    return HttpResponse("stubbo")

class UserPathNodeViewSet(viewsets.ModelViewSet):
    queryset = UserPathNode.objects.all()
    serializer_class = UserPathNodeSerializer
