from django.contrib.auth.models import User
from django.db import models


class Favorite(models.Model):
    """
    Model Favorite
    """
    owner = models.ForeignKey(User, related_name='favorites')
    content = models.URLField()
    description = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)
