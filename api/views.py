from django.shortcuts import render
from rest_framework import viewsets
from .utils import ver, deletehoneypot
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

    def destroy(self, request,pk):
        instance=self.get_object()
        deletehoneypot(instance.container_id)
        self.perform_destroy(instance)
        return Response(status=204)

class TriggersViewSet(viewsets.ModelViewSet):
    permission_classes=[AllowAny]
    queryset = Trigger.objects.all() # pylint: disable=no-member
    serializer_class = TriggerSerializer