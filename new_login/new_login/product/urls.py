from django.urls import path
from .views import ProductView, CartView, createorder


urlpatterns = [
    path('', ProductView, name='product'),
    path('cart_add/<int:id>/', CartView, name='cart'),
    path('create_order/<str:pk>/', createorder, name='Create_Order'),    
]
