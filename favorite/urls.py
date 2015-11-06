from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from favorite import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^favorites/$', views.FavoriteList.as_view()),
    url(r'^favorites/(?P<pk>[0-9]+)/$', views.FavoriteDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
