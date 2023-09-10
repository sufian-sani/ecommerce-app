from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View

from django.http import HttpResponse
# Create your views here.

class Blog(View):
    def get(self, request):
        activate="blog"
        # <view logic>
        return render(request,'blog/blog.html',{'activate':activate})

