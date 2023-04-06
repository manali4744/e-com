from django.shortcuts import render, redirect
from product.models import Product
from django.shortcuts import get_object_or_404

def add_to_cart(request, pk):

    product = get_object_or_404(Product, id=pk)

    if 'cart' not in request.session:
        request.session['cart'] = {}
    cart = request.session['cart']
    if pk in cart:
        cart[pk]['quantity'] += 1
    else:
        cart[pk] = {
            'product_id': product.id,
            'name': product.name,
            'price': product.price,
            'quantity': 1,
        }

    request.session.modified = True

    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    context = {
        'cart': cart,
    }
    return render(request, 'view_cart.html', context)