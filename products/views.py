from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from django.views import View


class ShopView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'shop.html', {'products': products})


class BuyView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        return render(request, 'buy-section.html', {'product': product})

