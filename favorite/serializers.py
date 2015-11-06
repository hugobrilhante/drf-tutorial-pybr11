from rest_framework import serializers

from favorite.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('pk', 'content', 'description', 'create')
