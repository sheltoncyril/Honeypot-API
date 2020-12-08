from rest_framework import serializers, viewsets
from .models import User, HoneypotTemplate, Honeypot, Trigger
from rest_framework.authtoken.models import Token
from .utils import createhoneypot

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_login', 'username', 'first_name', 'last_name', 'honeypots']

class HoneypotTemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HoneypotTemplate
        fields = ['id', 'name', 'image','config','url']

class HoneypotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Honeypot
        fields = ['id', 'name','template', 'container_ip','container_port', 'container_id', 'user', 'triggers' ]
    
    def create(self, validated_data):
        validated_data.pop("triggers")
        template=validated_data['template']
        cont=createhoneypot(template.config)
        cont.reload()
        validated_data['container_ip']=cont.attrs["NetworkSettings"]["Ports"]["80/tcp"][0]["HostIp"]
        validated_data['container_port']=cont.attrs["NetworkSettings"]["Ports"]["80/tcp"][0]["HostPort"]
        validated_data['container_id']=cont.short_id
        return Honeypot.objects.create(**validated_data)  # pylint: disable=no-member
    

class TriggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trigger
        fields = ['id','Honeypot','source_ip','port', 'username', 'password', 'log_time', 'full_log']
