from django.conf.urls import url
from favorite import views

urlpatterns = [
    url(r'^favorite/$', views.favorite_list),
    url(r'^favorite/(?P<pk>[0-9]+)/$', views.favorite_detail),
]
