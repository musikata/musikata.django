from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import UserPathNode
from .serializers import UserPathNodeSerializer


def get_userpathnode(request):
    return HttpResponse("stubbo")

class UserPathNodeViewSet(viewsets.ModelViewSet):
    queryset = UserPathNode.objects.all()
    serializer_class = UserPathNodeSerializer
