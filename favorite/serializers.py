from django.contrib.auth.models import User
from rest_framework import serializers


from favorite.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Favorite
        fields = ('pk', 'content', 'description', 'create', 'owner')


class UserSerializer(serializers.ModelSerializer):
    favorites = serializers.PrimaryKeyRelatedField(many=True, queryset=Favorite.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'favorites')
