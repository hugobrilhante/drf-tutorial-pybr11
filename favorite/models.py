from django.db import models


class Favorite(models.Model):
    """
    Modelo Favoritos
    """
    content = models.URLField()
    description = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)
