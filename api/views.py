from django.shortcuts import render
from rest_framework import viewsets
from .utils import ver
from rest_framework.permissions import IsAuthenticated
from .models import User, Honeypot
from .serializers import UsersSerializer, HoneypotsSerializer
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

class HoneypotsViewSet(viewsets.ModelViewSet):
    queryset = Honeypot.objects.all()
    serializer_class = HoneypotsSerializer
