from rest_framework import viewsets
from django_blogposts.rest.serializers import BlogPostSerializer
from django_blogposts.views import _get_queryset
from django_blogposts.models.blogpost import BlogPost


class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        return _get_queryset(
            self.request, self.queryset
        )
