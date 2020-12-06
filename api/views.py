from django.shortcuts import render
from rest_framework import viewsets
from .utils import ver
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User, HoneypotTemplate, Honeypot, Trigger
from .serializers import UsersSerializer, HoneypotTemplateSerializer, HoneypotSerializer, TriggerSerializer
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView


class UsersViewSet(viewsets.ModelViewSet):
    permission_classes=(IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class UserView(RetrieveAPIView):
    def get(self, request,format=None):
        ser = UsersSerializer(request.user)
        return Response(ser.data)

class HoneypotTemplatesViewSet(viewsets.ModelViewSet):
    queryset = HoneypotTemplate.objects.all() # pylint: disable=no-member
    serializer_class = HoneypotTemplateSerializer

class HoneypotsViewSet(viewsets.ModelViewSet):
    queryset = Honeypot.objects.all() # pylint: disable=no-member
    serializer_class = HoneypotSerializer

class TriggersViewSet(viewsets.ModelViewSet):
    permission_classes=[AllowAny]
    queryset = Trigger.objects.all() # pylint: disable=no-member
    serializer_class = TriggerSerializer