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


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ('user',)

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return self.request.user.project_user.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        return self.request.user.project_user.get(pk=pk)
