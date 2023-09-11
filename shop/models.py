from django.db import models
from colorfield.fields import ColorField

from category.models import Category
from django.urls import reverse
# Create your models here.


class Color(models.Model):
    color=ColorField()

    def __str__(self):
        return self.color
    
class Size(models.Model):
    size=models.CharField(max_length=2)
    
    def __str__(self):
        return self.size
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    review=models.CharField(max_length=255,blank=True)
    price = models.IntegerField()
    dicount_price=models.IntegerField(null=True,blank=True)
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField(blank=True)
    available_color = models.ManyToManyField(Color,blank=True,related_name='available_color')
    available_size = models.ManyToManyField(Size,blank=True,related_name='available_size')
    images = models.ImageField(upload_to = 'photo/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    def __str__(self):
        return self.product_name