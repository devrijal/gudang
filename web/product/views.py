import json
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from . models import ProductStok

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from . serializer import UserSerializer, GroupSerializer


def stok(request):
    all = ProductStok.objects.all().values().annotate(total=Count('ProductStokPK')).order_by('ProductIDF__ProductName')
    result = json.dumps(all)
    return HttpResponse(result)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
