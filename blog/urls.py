from django.urls import path
from . views import *

app_name = 'blog'

urlpatterns = [
    path("", Blog.as_view(),name='blog'),
]