from django.shortcuts import render
from posts.models import Post

# Create your views here.
def do_search(request):
    posts = Post.objects.filter(content__icontains=request.GET['q'])
    return render(request, "posts.html", {"posts": posts})
    
