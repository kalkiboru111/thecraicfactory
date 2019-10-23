from django.shortcuts import render, get_object_or_404
from .models import Product
from posts.models import Post, PostProduct

# Create your views here.
def all_products(request, pk):
    products = Product.objects.all()
    post = get_object_or_404(Post, pk=pk)
    post_product = get_object_or_404(PostProduct, pk=pk)
    print(post.id)
    print(post_product.id)
    return render(request, "products.html", {"products": products, "post": post, "post_product": post_product})