from django.conf.urls import url,include
from .views import *
urlpatterns = [
    url(r'list', company_list, name='company_list'),
]
