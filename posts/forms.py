from django import forms
from .models import Post

class BlogPostForm(forms.ModelForm):
    '''
    Form for posting posts to newsfeed. 
    '''
    class Meta:
        model = Post
        fields = ('title', 'content', 'published_date', 'image', 'tag')
        
    