from .models import *
from rest_framework.fields import CurrentUserDefault
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import viewsets, mixins
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from apps.rest_permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class LanguageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    http_method_names = ['get', 'head']
