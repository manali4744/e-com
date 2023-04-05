from django.urls import path
from .views import home, OtpView, RegisterPage, main, demo , logoutUser

urlpatterns = [
    path('', main, name = 'main' ),
    
    path('login/', home, name = 'login' ),
    path('logout/', logoutUser, name='logout'),
    path('register/', RegisterPage, name='register'),
    path('otp/', OtpView, name = 'otp'), 
    
    path('demo/', demo, name='demo'),

    # path('main/', main, name = 'main' ),
]
