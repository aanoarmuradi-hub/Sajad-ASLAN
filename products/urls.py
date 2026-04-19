from django.urls import path
from .views import UpdateProductView,AddProductView,ProductListView


urlpatterns = [
    path("add/", AddProductView.as_view()),
    path('update/<int:pk>/', UpdateProductView.as_view()),
    path("product/",ProductListView.as_view()),
  
    
]