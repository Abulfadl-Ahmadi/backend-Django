from post.models import Post
from user.models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'bio',
            'email',
            'image',
            'created_at',
        ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'user',
            'title',
            'content',
            'image',
            'update',
            'created_at',
            'status',
        ]

    # user = serializers.HyperlinkedIdentityField(view_name='user-api') 