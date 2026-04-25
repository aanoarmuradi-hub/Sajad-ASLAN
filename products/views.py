from rest_framework.views import APIView
from .models import Product
from django.views import View
from django.shortcuts import render, redirect
import requests


class ShopView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'shop.html', {'products': products})


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


