from django.shortcuts import render, get_object_or_404
from .models import Product
from posts.models import Post

# Create your views here.
def all_products(request, id=None):
    products = Product.objects.all()
    post = get_object_or_404(Post, id=id)
    return render(request, "products.html", {"products": products, "post": post})