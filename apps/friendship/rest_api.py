from .models import *
from rest_framework.fields import CurrentUserDefault
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import viewsets, mixins
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from apps.rest_permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'
        depth = 1
        # exclude = ['user',]


class FriendViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    permission_classes = (IsAuthenticated,)
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def get_queryset(self):
        return self.request.user.friend_user.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        return self.request.user.friend_user.get(pk=pk)


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'
        depth = 1
        # exclude = ['user',]


class BlockViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    permission_classes = (IsAuthenticated,)
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

    def get_queryset(self):
        return self.request.user.blocking.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        return self.request.user.blocking.get(pk=pk)

    def perform_update(self, serializer):
        serializer.save(blocker=self.request.user)
