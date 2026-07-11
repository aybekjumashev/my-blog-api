from django.core.cache import cache
from .models import Post, Category, Tag, Comment, User
from django.db.models import Count

def get_statistics():
    stats = cache.get('statistics')

    if not stats:
        total_posts = Post.objects.count()
        total_categories = Category.objects.count()
        total_tags = Tag.objects.count()
        total_comments = Comment.objects.count()
        total_users = User.objects.count()

        stats = {
            'total_posts': total_posts,
            'total_categories': total_categories,
            'total_tags': total_tags,
            'total_comments': total_comments,
            'total_users': total_users,
            'status': 'active'
        }
        
        cache.set('statistics', stats, 60 * 30)

    return stats