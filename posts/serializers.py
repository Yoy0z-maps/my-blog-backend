from rest_framework import serializers
from .models import Post
from users.serializers import ProfileSerializer

# 모델의 모든 필드
class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True) # nested serializer

    class Meta:
        model = Post
        fields = ("id", "title", "body", "image", "profile", "likes", "published_date", "category")
# 유저가 직접 입력하는 모델
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "body", "image", "tags", "category")
