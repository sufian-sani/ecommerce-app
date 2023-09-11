from django.urls import path
from . views import *

urlpatterns = [
    path("", Shop.shop,name='shop'),
    path('<slug:category_slug>/<slug:product_slug>',product_detail,name='product_detail'),
]