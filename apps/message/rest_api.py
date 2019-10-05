from .models import *
from rest_framework.fields import CurrentUserDefault
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import viewsets, mixins
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from apps.rest_permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        # fields = '__all__'
        depth = 1
        exclude = ['user', ]


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        return self.request.user.message_user.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        return self.request.user.message_user.get(pk=pk)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
