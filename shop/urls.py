from django.urls import path
from . views import *

app_name = 'shop'

urlpatterns = [
    path("", Shop.as_view(),name='shop'),
]