from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name', 'price', 'stock', 'category', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product,ProductAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display=["color"]

admin.site.register(Color,ColorAdmin)

class SizeAdmin(admin.ModelAdmin):
    list_display=["size"]

admin.site.register(Size,SizeAdmin)