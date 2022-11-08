from rest_framework import serializers
from .models import Post


class ProductSerializer(serializers.ModelSerializer):
    
    def create(self):
        Post = Post.objects.create()
        return Post


