from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from favorite.views import FavoriteViewSet, UserViewSet, api_root

favorite_list = FavoriteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
favorite_detail = FavoriteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^favorites/$', favorite_list, name='favorite-list'),
    url(r'^favorites/(?P<pk>[0-9]+)/$', favorite_detail, name='favorite-detail'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
])