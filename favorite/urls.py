from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from favorite import views

urlpatterns = [
    url(r'^favorite/$', views.favorite_list),
    url(r'^favorite/(?P<pk>[0-9]+)/$', views.favorite_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)