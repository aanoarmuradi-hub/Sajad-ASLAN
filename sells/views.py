from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import sell_product
from .serializers import SellSerializer

class SellProductView(APIView):

    def post(self, request):

        sell = sell_product(
            current_user = request.user,
            product_id=request.data.get("product_id"),
            quantity=int(request.data.get("quantity")),
        )

        serializer = SellSerializer(sell)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
