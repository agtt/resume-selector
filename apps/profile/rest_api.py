from .models import *
from rest_framework.fields import CurrentUserDefault
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import viewsets, mixins
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from apps.rest_permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        # fields = '__all__'
        depth = 1
        exclude = ['user', ]


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = None

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def get_object(self):
        try:
            return UserProfile.objects.get(user=self.request.user)
        except UserProfile.DoesNotExist:
            pass

    def perform_update(self, serializer):
        serializer.save(user=self.request.user, industry_id=int(self.request.data['industry']))
