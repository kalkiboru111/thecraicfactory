from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm
from django.contrib.auth.models import User

# Create your views here.

@login_required
def get_posts(request):
    '''
    This will create a view that will return a list of posts that were published prior to now. 
    '''
    posts = Post.objects.filter(published_date__lte=timezone.now
    ()).order_by('-published_date')
    return render(request, 'posts.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    '''
    Creat view that returns a single post object based on the post ID and render it to the postdetail.html... otherwise return a 404.
    '''
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, 'postdetail.html', {'post': post})
    
@login_required
def create_or_edit_post(request, pk=None):
    ''' 
    Create a view that allows us to create or edit a post depending if the post ID is null or not. 
    '''
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST": 
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'postform.html', {'form': form}) 

@login_required
def add_vote(request, pk):
    '''
    Creat view that returns a single post object based on the post ID and enables a user to vote for it... otherwise return a 404.
    '''
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST": 
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.upvotes=post.votes.up.user
            instance.downvotes=post.votes.down.user
            instance.devote=post.votes.delete.user
            instance.votes = post.votes.count()
            post=form.save()
        else:
            form = BlogPostForm(instance=post)
        return redirect(post_detail, post.pk)





# # Returns all instances voted by user
# Review.votes.all(user_id)