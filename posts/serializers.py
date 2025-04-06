from rest_framework import serializers
from .models import Post
from users.serializers import ProfileSerializer
import json

# 모델의 모든 필드
class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True) # nested serializer

    class Meta:
        model = Post
        fields = ("id", "title", "body", "image", "profile", "likes", "published_date", "category", "tags", "summary")
# 유저가 직접 입력하는 모델
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "body", "image", "tags", "category", "summary")

    def validate_tags(self, value):
        if isinstance(value, str):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                raise serializers.ValidationError("Invalid JSON for tags field")
        if not isinstance(value, list):
            raise serializers.ValidationError("tags must be a list")
        return value
