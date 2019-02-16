from django.conf.urls import url,include
from .views import *
urlpatterns = [
    url(r'create', EducationCreate.as_view(), name='education_create'),
    url(r'', EducationList.as_view(), name='education_list'),
]
