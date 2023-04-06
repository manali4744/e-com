from django.shortcuts import render, redirect, HttpResponse
from .forms import CreateUserforms
from .models import User, Customer
from product.models import Order
import random
import os
from twilio.rest import Client 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
# Create your views here.

def Send_OTP(OTP):
    account_sid = "AC0658569caf59ad3eb3722f28b9795726"
    auth_token  = "f76e089823c608b69a201ae760f3b0c8"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body= OTP,
    from_="+14406368067",
    to="+918140987675"
    )
@login_required(login_url='/login/')
def main(request):
    user = request.user
    print(user.name)
    user_cust = Customer.objects.get(Customer=user)
    order = Order.objects.filter(customer=user_cust)
    context = {
        'name': user.name,
        'order' : order
               
    }
    return  render(request, 'user/welcome.html', context)

def demo(request):
    return render(request, 'user/main.html')

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if '@' and '.' in username:
            try:
                context = {'email': username}
                ex_user = User.objects.get(email=username)
                print(ex_user.email)
                OTP = random.randint(100000, 999999)
                print(OTP)
                ex_user.otp = OTP
                ex_user.save()
                Send_OTP(OTP)
                return redirect('otp')
            except User.DoesNotExist as e :
                return redirect('register')
        else:
            try:
                context = {'phone': username}
                ex_user = User.objects.get(phone=username)
                print(ex_user.name, ex_user.phone)
                OTP = random.randint(100000, 999999)
                print(OTP)
                ex_user.otp = OTP
                ex_user.save()
                Send_OTP(OTP)
                return redirect('otp')
            except User.DoesNotExist as e :
                return redirect('register')
    return render(request, 'user/home.html')

def OtpView(request):
    if request.method == 'POST':
        try:
            otp = request.POST.get('otp')
            verify_otp = User.objects.get(otp=otp)
            print(otp)
            print(verify_otp.name)
            context = {"name": verify_otp.name}
            if otp == verify_otp.otp:
                print(verify_otp.otp)
                verify_otp.otp = None
                verify_otp.save()
                login(request, verify_otp)
                return redirect('/')
                # return redirect('/')
                messages.info(request, 'OTP  is incorrect')
                print("wrong OTP")
                
        except User.DoesNotExist :
            messages.info(request, 'OTP is wrong')
            return render(request, 'user/otp.html')   
    return render(request, 'user/otp.html')

def RegisterPage(request):
    form = CreateUserforms()
    if request.method == "POST":
        form = CreateUserforms(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('name')
            phone = form.cleaned_data.get('phone')
            ex_user = User.objects.get(phone=phone)
            OTP = random.randint(100000, 999999)
            ex_user.otp = OTP
            ex_user.save()
            Send_OTP(OTP)
            Customer.objects.create(Customer=ex_user)
            messages.success(request, 'Account was created for ' + username)
            return redirect('otp')
    context = {'form': form}
    return render(request, 'user/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')



