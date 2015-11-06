from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from favorite.models import Favorite
from favorite.serializers import FavoriteSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def favorite_list(request):
    """
    List all favorite, or create a new favorite.
    """
    if request.method == 'GET':
        favorites = Favorite.objects.all()
        serializer = FavoriteSerializer(favorites, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FavoriteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def favorite_detail(request, pk):
    """
    Retrieve, update or delete a code favorite.
    """
    try:
        favorite = Favorite.objects.get(pk=pk)
    except Favorite.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FavoriteSerializer(favorite)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FavoriteSerializer(favorite, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        favorite.delete()
        return HttpResponse(status=204)
