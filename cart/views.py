from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from posts.models import Post

# Create your views here.
@login_required
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")

@login_required
def add_to_cart(request, id, pk):
    quantity = int(request.POST.get('quantity'))
    post = get_object_or_404(Post, pk)

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    render(request, "cart.html", {"post": post})

@login_required
def adjust_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))