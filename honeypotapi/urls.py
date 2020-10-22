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

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','url', 'username', 'email', 'is_staff', 'containers']

class HoneypotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Honeypot
        fields = ['id','name', 'container_id', 'container_ip', 'container_conf', "user"]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)
    


class HoneypotViewSet(viewsets.ModelViewSet):
    queryset = Honeypot.objects.all()
    serializer_class = HoneypotSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'honeypot', HoneypotViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
