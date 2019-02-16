from django.conf.urls import url,include
from .views import *
urlpatterns = [
    url(r'create', ExperienceCreate.as_view(), name='experience_create'),
    url(r'', ExperienceList.as_view(), name='experience_list'),
]
