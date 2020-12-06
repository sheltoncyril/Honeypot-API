from rest_framework import serializers, viewsets
from .models import User, Honeypot
from rest_framework.authtoken.models import Token


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_login', 'username', 'first_name', 'last_name', 'containers']

class HoneypotsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Honeypot
        fields = '__all__'
