from .models import Product
from users.services import require_role

def add_product(current_user, name, price, stock,image=None):

    require_role(current_user, ["admin"])

    if not name:
        raise ValueError("Enter product name")

    if price <= 0:
        raise ValueError("Price must be positive")

    if stock < 0:
        raise ValueError("Stock must not be negative")

    product = Product.objects.create(
        name=name,
        price=price,
        stock=stock,
        image=image
    )

    return product


def update_product(current_user, product_id, name, price, stock):

    require_role(current_user, ["admin"])

    
    product = Product.objects.get(id=product_id)

    if price < 0:
        raise ValueError("Price must be positive")

    if stock < 0:
        raise ValueError("Stock must be positive")

    product.name = name
    product.price = price
    product.stock = stock
    product.save()

    return product