from django.urls import path
from .views import PostViewSet, UserViewSet, CategoryViewSet, TagViewSet, StatisticsViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'statistics', StatisticsViewSet, basename='statistics')
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls