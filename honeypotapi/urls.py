"""honeypotapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from api.models import User, Honeypot
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import obtain_auth_token

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','url', 'username','first_name', 'last_name', 'email', 'is_staff', 'containers']

class HoneypotsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Honeypot
        fields = ['id', 'url', 'name', 'container_id', 'container_ip', 'container_conf', "user"]

class UsersViewSet(viewsets.ModelViewSet):
    permission_classes=(IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class HoneypotsViewSet(viewsets.ModelViewSet):
    queryset = Honeypot.objects.all()
    serializer_class = HoneypotsSerializer

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'honeypots', HoneypotsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
