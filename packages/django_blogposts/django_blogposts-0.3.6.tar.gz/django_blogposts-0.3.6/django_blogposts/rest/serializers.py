from rest_framework import serializers
from django_blogposts.models import BlogPost, Tags


class TagsSerializer(serializers.ModelSerializer):
    absolute_url = serializers.CharField(source='get_absolute_url')
    class Meta:
        model = Tags
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    absolute_url = serializers.CharField(source='get_absolute_url')
    image = serializers.CharField(source='image.url')
    tags = TagsSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        exclude = ('content', 'meta_title', 'meta_kw', 'meta_desc', 'de',)
