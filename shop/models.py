from django.db import models
from colorfield.fields import ColorField

from category.models import Category
from django.urls import reverse
# Create your models here.


class Variation(models.Model):
    color=ColorField()
    size=models.CharField(max_length=2)
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    review=models.CharField(max_length=255,blank=True)
    price = models.IntegerField()
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField(max_length=500,blank=True)
    available_color = models.ForeignKey(Variation,null=True,blank=True,on_delete=models.DO_NOTHING,related_name='available_color')
    available_size = models.ForeignKey(Variation,null=True,blank=True,on_delete=models.DO_NOTHING,related_name='available_size')
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