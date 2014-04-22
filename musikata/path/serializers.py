from .models import UserPathNode
from rest_framework import serializers


class UserPathNodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserPathNode
        #fields = ('user', 'path_node',)
        fields = ('id',)
