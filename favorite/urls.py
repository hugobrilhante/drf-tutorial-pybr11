from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from favorite import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^favorites/$', views.FavoriteList.as_view(), name='favorite-list'),
    url(r'^favorites/(?P<pk>[0-9]+)/$', views.FavoriteDetail.as_view(), name='favorite-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
