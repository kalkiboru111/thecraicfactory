from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm

# Create your views here.

def get_posts(request):
    '''
    This will create a view that will return a list of posts that were published prior to now. 
    '''
    posts = Post.objects.filter(published_date__lte=timezone.now
    ()).order_by('-published_date')
    return render(request, 'posts.html', {'posts': posts})

def post_detail(request, pk):
    '''
    Creat view that returns a single post object based on the post ID and render it to the postdetail.html... otherwise return a 404.
    '''
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, 'postdetail.html', {'post': post})
    
def create_or_edit_post(request, pk=None):
    ''' 
    Create a vie w that allows us to create or edit a post depending if the post ID is null or not. 
    '''
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST": 
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'postform.html', {'form': form}) 
