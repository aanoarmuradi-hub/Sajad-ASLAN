
from django.db import transaction
from products.models import Product
from .models import Sell
from users.services import require_role

def sell_product(current_user, product_id, quantity):

    require_role(current_user, ["admin", "user"])

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    with transaction.atomic():

        product = Product.objects.select_for_update().get(id=product_id)

        if product.stock < quantity:
            raise ValueError("Not enough stock")

        product.stock -= quantity
        product.save()

        total_price = product.price * quantity

        sell = Sell.objects.create(
            product=product,
            quantity=quantity,
            total_price=total_price,
            sold_by=current_user
        )

    return sell