from .models import *
from rest_framework.fields import CurrentUserDefault
from rest_framework.views import APIView
from rest_framework import viewsets , mixins,generics ,serializers
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from apps.rest_permissions import IsAuthenticatedOrReadOnly
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    http_method_names = ['get', 'head']

    # def get_queryset(self):
    #     return self.request.user.company_user.all()
    #
    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     return self.request.user.company_user.get(pk=pk)
