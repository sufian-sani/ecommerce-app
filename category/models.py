from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse


class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank = 
    True, null=True)
    title = models.CharField(max_length=100) 
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:

        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     

    def get_url(self):
        return reverse('products_by_category',args=[self.slug])