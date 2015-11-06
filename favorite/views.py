from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from favorite.models import Favorite
from favorite.serializers import FavoriteSerializer


@api_view(['GET', 'POST'])
def favorite_list(request, format=None):
    """
    List all favorite, or create a new favorite.
    """
    if request.method == 'GET':
        favorite = Favorite.objects.all()
        serializer = FavoriteSerializer(favorite, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def favorite_detail(request, pk, format=None):
    """
    Retrieve, update or delete a favorite instance.
    """
    try:
        favorite = Favorite.objects.get(pk=pk)
    except Favorite.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FavoriteSerializer(favorite, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
