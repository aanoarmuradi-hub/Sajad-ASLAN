from django.urls import path
from .views import AddUserView,ViewUser,DashboardStats

urlpatterns = [
    path('users/', AddUserView.as_view()),
    path('user/info/',ViewUser.as_view()),
    path('dashboard/stats/',DashboardStats.as_view()),
    
    ]