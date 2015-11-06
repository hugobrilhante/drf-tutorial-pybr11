from rest_framework import serializers

from favorite.models import Favorite


class FavoriteSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    content = serializers.URLField()
    description = serializers.CharField(required=True, allow_blank=False, max_length=100)
    create = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create and return a new `Favorite` instance, given the validated data.
        :param validated_data:
        """
        return Favorite.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Favorite` instance, given the validated data.
        """

        instance.content = validated_data.get('content', instance.content)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
