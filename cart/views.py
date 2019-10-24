from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from posts.models import Post
from posts.models import Product
from django.http import HttpResponseRedirect
from checkout.models import OrderLineItem

@login_required
def add_to_cart(request, id, pk):
    #product_id = request.POST['product']
    product_id = id
    post = pk
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if product_id in cart:
        if post in cart[product_id]:
            cart[product_id][post] += quantity
        else:
            cart[product_id].update({post:quantity})
    else:
        cart[product_id]={post:quantity}
    
    # if post in cart:
    #     if product_id in cart[post]:
    #         cart[post][product_id] += quantity
    #     else:
    #         cart[post].update({product_id:quantity})
    # else:
    #     cart[post]={product_id:quantity}
    
    #cart[id] = cart.get(id, quantity, pk)

    request.session['cart'] = cart
    print('*****************************')
    print(cart)  
    return render(request, "cart2.html", {"post": post, "product_id": product_id})
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Create your views here.
@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    cart_total =0
    
    for product_id, post in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        for post, quantity in post.items():
            
            cart_items.append({
                'id': product.id,
                'name': product.name,
                'post': post,
                'description': product.description,
                'quantity': quantity,
                'total': product.price * quantity,
                })  
            
            cart_total += product.price * quantity
    
    return render(request, "cart2.html", {'cart_items': cart_items, 'cart_total': cart_total})


@login_required
def adjust_cart(request):
    product_id = request.POST['product']
    post = request.POST['post']
    cart = request.session.get('cart', {})
    del cart[product_id][post]
    request.session['cart'] = cart
    # if quantity > 0:
    #     cart[id] = quantity
    # else:
    #     cart.pop(id)
    #request.session['cart'] = cart
    render(request, "cart2.html")