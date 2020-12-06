from django.contrib import admin
from django.urls import path, include
from .views import UsersViewSet, HoneypotsViewSet, UserView
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'honeypots', HoneypotsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('user/',UserView.as_view(), name="userview"),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]