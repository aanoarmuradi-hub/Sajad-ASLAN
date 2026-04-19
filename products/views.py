from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import update_product,add_product
from .serializers import productSerializer
from rest_framework.generics import ListAPIView
from .models import Product
from django.views import View

class UpdateProductView(APIView):

    def put(self, request, pk):

        product = update_product(
            current_user = request.user,
            pk=pk,
            name=request.data.get("name"),
            price=float(request.data.get("price")),
            stock=int(request.data.get("stock")),
        )

        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)



class AddProductView(APIView):

    def post(self, request):
        image = request.FILES.get("image") 
        product = add_product(
            current_user = request.user,
            name=request.data.get("name"),
            price=float(request.data.get("price")),
            stock=int(request.data.get("stock")),
            image=image
        )
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer


class ShopView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'shop.html', {'products': products})


class BuyView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        return render(request, 'buy-section.html', {'product': product})

