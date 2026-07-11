from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name="Title")
    content = models.TextField(blank=True, verbose_name="Content")
    is_published = models.BooleanField(default=False, verbose_name="Is Published")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    view_count = models.IntegerField(default=0, verbose_name="View Count")
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author", related_name='posts')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name="Tags", related_name='posts')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Category", related_name='posts')
    
    likes = models.ManyToManyField(User, blank=True, verbose_name="Likes", related_name='liked_posts')
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Tag Name")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category Name")

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="Post")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name="Author")
    content = models.TextField(verbose_name="Comment")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    
    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'