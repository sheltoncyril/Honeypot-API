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
from api.utils import ver
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_login', 'username', 'first_name', 'last_name', 'containers']

class HoneypotsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Honeypot
        fields = '__all__'

class UsersViewSet(viewsets.ModelViewSet):
    permission_classes=(IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class UserView(RetrieveAPIView):
    def get(self, request,format=None):
        ser = UsersSerializer(request.user)
        return Response(ser.data)

class HoneypotsViewSet(viewsets.ModelViewSet):
    queryset = Honeypot.objects.all()
    serializer_class = HoneypotsSerializer

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
