from django.db import models
from django.contrib.auth.models import User


class PathNode(models.Model):
    pass

class UserPathNode(models.Model):
    user = models.ForeignKey(User)
    path_node = models.ForeignKey(PathNode)
