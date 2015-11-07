from django.conf.urls import url, include
from favorite import views
from rest_framework_nested import routers

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
favorite_router = routers.NestedSimpleRouter(router, r'users', lookup='owner')
favorite_router.register(r'favorites', views.FavoriteViewSet, base_name='user-favorite')

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(favorite_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]