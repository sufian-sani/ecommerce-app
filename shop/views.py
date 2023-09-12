from django.shortcuts import render
from django.shortcuts import render,get_object_or_404

from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.
from django.shortcuts import render
from django.views import View
from .models import *

from django.http import HttpResponse
# Create your views here.

class Shop(View):
    def shop(request,category_slug=None):
        activate = 'shop'
        categories = None
        products = None
        if category_slug !=None:
            categories = get_object_or_404(Category,slug=category_slug)
            products = Product.objects.filter(category=categories,is_available=True)
            paginator = Paginator(products,3)
            page = request.GET.get('page')
            paged_products = paginator.get_page(page)
            product_count = products.count()
            # product_image=products.images.url
        else:
            products = Product.objects.all().filter(is_available=True).order_by('id')
            paginator = Paginator(products,10)
            page = request.GET.get('page')
            paged_products = paginator.get_page(page)
            product_count = products.count()
            # product_image=products.images.url
        context = {
            'products':paged_products,
            'product_count':product_count,
            'activate':activate,
        }
        # import pdb
        # pdb.set_trace()
        return render(request,'shop/shop.html',context)

def product_detail(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
        
        print("ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",single_product.available_color)
    except Exception as e:
        raise e
    context={
        'single_product':single_product,
    }
    return render(request,'shop/product_details.html',context)