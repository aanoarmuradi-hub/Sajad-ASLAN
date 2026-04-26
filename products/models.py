from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/', null=True, blank=True) 
    image_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
