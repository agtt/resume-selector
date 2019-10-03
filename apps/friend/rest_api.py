from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block

from rest_framework.fields import CurrentUserDefault
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import viewsets, mixins
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from apps.rest_permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated


class FriendSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'
        # exclude = ['to_user','from_user']


class FriendViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    permission_classes = (IsAuthenticated,)
    queryset = Friend.objects.all()
    serializer_class = FriendSeriliazer

    def get_queryset(self):
        return Friend.objects.friends(self.request.user)
