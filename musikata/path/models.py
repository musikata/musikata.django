from django.db import models
from django.contrib.auth.models import User


class PathNode(models.Model):
    path_id = models.CharField(max_length=255, null=True)
    xpath = models.CharField(max_length=255, null=True)

class UserPathNode(models.Model):
    user = models.ForeignKey(User)
    path_node = models.ForeignKey(PathNode)
    status = models.CharField(max_length=255, null=True)
