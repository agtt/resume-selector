from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from apps.experience.rest_api import *
from apps.education.rest_api import *
from apps.project.rest_api import *
from apps.job.rest_api import *
from apps.company.rest_api import *
from apps.skill.rest_api import *
from apps.language.rest_api import *
from apps.profile.rest_api import *
from apps.post.rest_api import *
from apps.friendship.rest_api import *
from apps.question.rest_api import *
from apps.message.rest_api import *
from apps.user.rest_api import *

router = routers.DefaultRouter()
router.register(r'experience', ExperienceViewSet)
router.register(r'education', EducationViewSet)
router.register(r'project', ProjectViewSet)
router.register(r'job', JobViewSet)
router.register(r'industry', IndustryViewset)
router.register(r'section', SectionViewset)
router.register(r'company', CompanyViewSet)
router.register(r'skill', SkillViewSet)
router.register(r'language', LanguageViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'friend', FriendViewSet)
router.register(r'block', BlockViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'message', MessageViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls), name='api-main'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
