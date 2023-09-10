from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from .models import *

from django.http import HttpResponse
# Create your views here.

class Shop(View):
    def get(self, request):
        activate = 'shop'
        # <view logic>
        return render(request,'shop/shop.html',{'activate':activate})

def product_detail(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
        
        
    except Exception as e:
        raise e
    context={
        'single_product':single_product,
    }
    return render(request,'shop/product_details.html',context)