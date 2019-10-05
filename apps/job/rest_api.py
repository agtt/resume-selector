from .models import *
from rest_framework.fields import CurrentUserDefault
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, generics, serializers
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from apps.rest_permissions import IsAuthenticatedOrReadOnly
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.rest_pagination import LargePagination


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        exclude = ('user',)


class IndustrySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'
        http_method_names = ['get', 'head']


class SectionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
        http_method_names = ['get', 'head']


class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        return self.request.user.job_user.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        return self.request.user.job_user.get(pk=pk)


class IndustryViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Industry.objects.all()
    serializer_class = IndustrySerilizer
    pagination_class = LargePagination


class SectionViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Section.objects.all()
    serializer_class = SectionSerilizer
    pagination_class = LargePagination
