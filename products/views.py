from rest_framework.views import APIView
from .models import Product
from .models import Category, SubCategory
from django.views import View
from django.shortcuts import render, redirect
import requests
from .models import Product, Cart, CartItem
from django.contrib.auth.mixins import LoginRequiredMixin


class BuyView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        return render(request, 'buy-section.html', {'product': product})



class ViewProducts(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'products-list.html', {'products': products})



class ViewNewProduct(View):
    def get(self, request):
        products = Product.objects.all().order_by('-created_at')[:10]
        return render(request, 'new-products.html', {'products': products})


# 🏠 Home → فقط دسته‌ها
class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'shop.html', {'categories': categories})


# 📂 زیر دسته‌ها
class SubCategoryView(View):
    def get(self, request, category_id):
        subs = SubCategory.objects.filter(category_id=category_id)
        return render(request, 'subcategories.html', {'subs': subs})


# 🛍 محصولات
class ProductListView(View):
    def get(self, request, sub_id):
        products = Product.objects.filter(subcategory_id=sub_id)
        return render(request, 'products.html', {'products': products})
    


class AboutView(View):

    def get(self, request):

        return render(request, 'about.html')



class ContactView(View):

    def get(self, request):

        return render(request, 'contact.html')
    

class AddToCartView(LoginRequiredMixin, View):

    def get(self, request, id):

        product = Product.objects.get(id=id)

        cart, created = Cart.objects.get_or_create(
            user=request.user
        )

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )

        if created == False:

            cart_item.quantity += 1

            cart_item.save()

        return redirect('cart')
    



class CartView(LoginRequiredMixin, View):

    def get(self, request):

        cart = Cart.objects.get(user=request.user)

        cart_items = cart.items.all()

        total_price = 0

        for item in cart_items:

            total_price += item.product.price * item.quantity

        context = {

            'cart_items': cart_items,

            'total_price': total_price,
        }

        return render(request,'cart.html',context)
    

class RemoveCartItemView(LoginRequiredMixin,View):

    def get(self, request, id):
        cart_item = CartItem.objects.get(id=id)
        cart_item.delete()
        return redirect('cart')
    


class IncreaseQuantityView(LoginRequiredMixin, View):

    def get(self, request, id):

        cart_item = CartItem.objects.get(id=id)

        cart_item.quantity += 1

        cart_item.save()

        return redirect('cart')
    

class DecreaseQuantityView(LoginRequiredMixin,View):

    def get(self, request, id):

        cart_item = CartItem.objects.get(id=id)

        if cart_item.quantity > 1:

            cart_item.quantity -= 1

            cart_item.save()

        else:

            cart_item.delete()

        return redirect('cart')