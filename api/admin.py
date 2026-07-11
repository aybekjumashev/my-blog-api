from django.contrib import admin
from .models import Post, Category, Tag, Comment



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published', 'view_count', 'category', 'author')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)