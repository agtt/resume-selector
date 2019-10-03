from django.conf.urls import url,include

urlpatterns = [
    url(r'experience', include('apps.experience.urls'), name='experience'),
    url(r'education', include('apps.education.urls'), name='education'),
    url(r'company', include('apps.company.urls'), name='company'),
    url(r'^friendship/', include('apps.friendship.urls'))
]
