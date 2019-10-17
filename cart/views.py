from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from posts.models import Post
from posts.models import Product

# Create your views here.
@login_required
def view_cart(request):
    return render(request, "cart2.html")

@login_required
def add_to_cart(request, id, pk):
    quantity = int(request.POST.get('quantity'))
    post = get_object_or_404(Post, pk=pk)
    print(post.id)

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return render(request, "cart2.html", {"post": post})

@login_required
def adjust_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    render(request, "cart2.html")