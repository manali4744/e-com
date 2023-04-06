from django.shortcuts import render, redirect
from .models import Product, Order, Cart
from app.models import User, Customer
from django.contrib import messages 
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def ProductView(request):
    if request.method == 'POST':
        data = request.POST.get('product_id')
        product = Product.objects.get(id=data)
        context = {
            'id': data,
            'product':product
        }
        return render(request, 'product_detail.html', context)
    item = Product.objects.all()
    context = {
        "item" : item
    }
    return render(request, 'product.html', context)

@login_required(login_url='/login/') 
def CartProductView(request, pk):
    user = request.user
    cart_customer = Customer.objects.get(Customer=user)
    cart_item = Cart.objects.get(customer=cart_customer)
    product = Product.objects.get(id=pk)
    product_cart = cart_item.cart.all()
    context = {
        'id': pk,
        'product': product,
        'product_cart' : product_cart 
    }
    return render(request, 'product_detail.html', context)

@login_required(login_url='/login/')  
def CartAddView(request, pk):
    user = request.user
    cart_customer = Customer.objects.get(Customer=user)
    cart_item = Cart.objects.get(customer=cart_customer)
    product = Product.objects.get(id=pk)
    cart_item.cart.add(product.id)
    cart_item.save()
    product_cart = cart_item.cart.all()
    context = {
        'product' : product_cart
    }
   
    return render(request, 'cart.html', context)

@login_required(login_url='/login/')  
def CartView(request):
    user = request.user
    cart_customer = Customer.objects.get(Customer=user)
    cart_item = Cart.objects.get(customer=cart_customer)
    product_cart = cart_item.cart.all()
    context = {
        'product' : product_cart
    }
    return render(request, 'cart.html', context)

@login_required(login_url='/login/')  
def CartRemoveView(request, pk):
    user = request.user
    cart_customer = Customer.objects.get(Customer=user)
    cart_item = Cart.objects.get(customer=cart_customer)
    product = Product.objects.get(id=pk)
    cart_item.cart.remove(product.id)
    product_cart = cart_item.cart.all()
    context = {
        'product' : product_cart
    }
    return render(request, 'cart.html', context)

@login_required(login_url='/login/')
def CreateOrderView(request, pk):
    product = Product.objects.get(id=pk)
    form = OrderForm(initial={'product': product, 'customer':request.user})
    if request.method == 'POST':
        formset = OrderForm(request.POST, instance=product)
        if formset.is_valid():
            formset.save()
            customer_sub = formset.cleaned_data.get('customer')
            quantity = formset.cleaned_data.get('quantity')
            user = request.user
            customer = Customer.objects.get(Customer=user)
            Order.objects.create(customer=customer,product=product, quantity= quantity)
            context ={
                'customer': request.user.name,
                'phone': request.user.phone,
                'email': request.user.email,
                'name': product,
                'quantity': quantity,
                'price' : product.price,
                'payment_amount' : float(quantity*product.price)
            }
            return render(request, 'order_detail.html', context)

    context = {'formset': form}
    return render(request, 'order.html', context)

@login_required(login_url='/login/')
def OrderRemoveView(request, pk):
    order = Order.objects.get(date_created = pk)
    order.delete()
    return redirect('/')




