from rest_framework import serializers, viewsets
from .models import User, HoneypotTemplate, Honeypot, Trigger
from rest_framework.authtoken.models import Token


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_login', 'username', 'first_name', 'last_name', 'containers']

class HoneypotTemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HoneypotTemplate
        fields = ['id', 'name', 'image','config','url']

class HoneypotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Honeypot
        fields = ['name','template', 'container_ip', 'container_id', 'user', 'triggers' ]

class TriggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trigger
        fields = ['id','Honeypot','source_ip','port', 'username', 'password', 'log_time']
