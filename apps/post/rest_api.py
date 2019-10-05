from .models import *
from rest_framework.fields import CurrentUserDefault
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import viewsets, mixins
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from apps.rest_permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated


class PostSerializer(serializers.ModelSerializer):
    comment_post = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        # fields = '__all__'
        depth = 1
        exclude = ['user', ]


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.request.user.post_user.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        return self.request.user.post_user.get(pk=pk)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = '__all__'
        depth = 1
        exclude = ['user', ]


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.request.user.comment_user.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        return self.request.user.comment_user.get(pk=pk)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, post_id=int(self.request.data['post']))
