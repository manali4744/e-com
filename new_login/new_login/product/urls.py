from django.urls import path
from .views import ProductView, CartAddView, CartView, CreateOrderView, CartRemoveView, CartProductView, OrderRemoveView


urlpatterns = [
    path('', ProductView, name='product'),

    path('cart/', CartView, name ='cart-view'),
    path('cart_add/<str:pk>/', CartAddView, name='cart'),
    path('cart_remove/<str:pk>', CartRemoveView, name ='cart-remove'),
    path('cart_product_view/<str:pk>', CartProductView, name ='cart-product-view'),

    path('create_order/<str:pk>/', CreateOrderView, name='Create_Order'),    
    path('remove_order/<str:pk>/', OrderRemoveView, name='remove_Order'),    
]
