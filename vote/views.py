from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Vote, Post
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.
@login_required
def upvote(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk)
        post.votes_total += 1
        # changes
        try:
            Vote.objects.create(post=post, user=request.user)
            post.save()
        except IntegrityError:  # if "unique_together" fails, it will raise an  "IntegrityError" exception
            return HttpResponse("vote not casted")

        return redirect('/posts/' + str(post.id))