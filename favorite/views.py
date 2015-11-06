from favorite.models import Favorite
from favorite.serializers import FavoriteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FavoriteList(APIView):
    """
    List all favorite, or create a new favorite.
    """
    def get(self, request, format=None):
        favorite = Favorite.objects.all()
        serializer = FavoriteSerializer(favorite, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class FavoriteDetail(APIView):
    """
    Retrieve, update or delete a favorite instance.
    """
    def get_object(self, pk):
        try:
            return Favorite.objects.get(pk=pk)


        except Favorite.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        favorite = self.get_object(pk)
        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        favorite = self.get_object(pk)
        serializer = FavoriteSerializer(favorite, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        favorite = self.get_object(pk)
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)