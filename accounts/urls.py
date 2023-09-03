from django.urls import path
from django.views.generic import TemplateView

app_name = 'accounts'

urlpatterns = [
    path('register', TemplateView.as_view(template_name='accounts/signup.html'),name='singup')
]