from django.shortcuts import render, redirect
from .models import Product, Order
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

    
def CartView(request):
    pass

@login_required(login_url='/login/')
def createorder(request, pk):
    print(request.user)
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

