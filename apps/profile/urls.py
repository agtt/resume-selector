from django.conf.urls import url
from .views import ProfileHomeView, ProfileIdentite
from allauth.account.views import SignupView, LoginView, PasswordResetView

class MySignupView(SignupView):
    template_name = 'allauth/signup.html'

class MyLoginView(LoginView):
    template_name = 'allauth/login.html'

class MyPasswordResetView(PasswordResetView):
    template_name = 'allauth/password_reset.html'

urlpatterns = [
    url(r'^$', ProfileHomeView.as_view(), name='profile-home'),
    url(r'^identity/(?P<pk>[0-9]+)/$',
        ProfileIdentite.as_view(), name='profile-identity-form'),
    url(r'^login', MyLoginView.as_view(), name='account_login'),
    url(r'^signup', MySignupView.as_view(), name='account_signup'),
    url(r'^password_reset', MyPasswordResetView.as_view(), name='account_reset_password'),
]
