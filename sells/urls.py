from django.urls import path
from .views import SellProductView

urlpatterns = [
    path('sells/', SellProductView.as_view()),
]