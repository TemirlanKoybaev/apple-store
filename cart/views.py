from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .cart import Cart
from django.contrib import messages

def cart_detail(request):
    cart = Cart(request)
    context = {
        'cart': cart,
        'total': cart.get_total_price(),
    }
    return render(request, 'cart/cart_detail.html', context)

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    messages.success(request, f'{product.name} добавлен в корзину!')
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f'{product.name} удален из корзины')
    return redirect('cart_detail')