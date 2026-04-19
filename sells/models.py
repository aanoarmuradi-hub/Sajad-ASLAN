from django.db import models
from products.models import Product
from users.models import User

class Sell(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    sold_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)
