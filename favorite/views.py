from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.filters import DjangoFilterBackend, SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from favorite.models import Favorite
from favorite.permissions import IsOwnerOrReadOnly
from favorite.serializers import FavoriteSerializer, UserSerializer


class DynamicFieldsMixin(object):
    def list(self, request, *args, **kwargs):
        fields = request.query_params.get('fields', None)
        if fields:
            fields = tuple(fields.split(','))
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, fields=fields)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True, fields=fields)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        fields = request.query_params.get('fields', None)
        if fields:
            fields = tuple(fields.split(','))
        instance = self.get_object()
        serializer = self.get_serializer(instance, fields=fields)
        return Response(serializer.data)


class UserViewSet(DynamicFieldsMixin, viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('username', 'email')
    search_fields = ('username', 'email')
    ordering_fields = ('username', 'email')
    pagination_class = LimitOffsetPagination


class FavoriteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('owner', 'content')
    search_fields = ('^owner__username', '^content')
    ordering_fields = ('owner', 'content')
    pagination_class = LimitOffsetPagination

    def list(self, request, owner_pk=None):
        queryset = self.queryset.filter(owner_id=owner_pk)
        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk, owner_pk=None):
        instance = self.queryset.get(pk=pk, owner_id=owner_pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
