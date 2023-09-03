from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View

from django.http import HttpResponse
# Create your views here.

class Shop(View):
    def get(self, request):
        activate = 'shop'
        # <view logic>
        return render(request,'shop/shop.html',{'activate':activate})

