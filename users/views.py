from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import add_user
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .models import User



class AddUserView(APIView):

    def post(self, request):

        user = add_user(
            current_user = request.user,
            username=request.data.get("username"),
            password=request.data.get("password"),
            role=request.data.get("role"),
        )

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ViewUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        
        return Response({
            "username": request.user.username,
            "role": request.user.role,
        })
        
class DashboardStats(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):

        return Response({
            "Total_Users":User.objects.count(),
            "Active_Users":User.objects.filter(is_active = True).count(),

        })



        




        
