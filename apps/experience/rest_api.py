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


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        # fields = '__all__'
        depth = 1
        exclude = ('user',)


class ExperienceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        return self.request.user.experience_user.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        try:
            return self.request.user.experience_user.get(pk=pk)
        except Experience.DoesNotExist:
            pass

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, company_id=int(self.request.data['company']),
                        industry_id=int(self.request.data['industry']))

# class ExperienceDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#
#     permission_classes = (IsAuthenticated,)
#
#     def get_object(self, pk):
#         try:
#             return Experience.objects.get(pk=pk)
#         except Experience.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = ExperienceSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = ExperienceSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
