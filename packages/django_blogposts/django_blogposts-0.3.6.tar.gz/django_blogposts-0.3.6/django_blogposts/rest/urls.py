from rest_framework.routers import DefaultRouter
from django_blogposts.rest.views import BlogPostViewSet


router = DefaultRouter()
router.register(r'posts', BlogPostViewSet)

urlpatterns = router.urls
