from django.urls import path
from django.views.generic import TemplateView
from .views import *

app_name = 'accounts'

urlpatterns = [
    # path('register', TemplateView.as_view(template_name='accounts/signup.html'),name='singup')
    path("register/", Signup.as_view(), name="singup"),
    path("signin/", Signin.as_view(), name="signin"),
    path("signout/", SignOutView.as_view(), name="signout"),
]