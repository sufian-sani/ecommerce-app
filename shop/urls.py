from django.urls import path
from . views import *

urlpatterns = [
    path("", Shop.as_view(),name='shop'),
]