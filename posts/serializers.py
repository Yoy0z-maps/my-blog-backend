from rest_framework import serializers
from .models import Post, Comment
from users.serializers import ProfileSerializer
import json

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "nickname", "text", "post")

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("nickname", "text", "post")

# 모델의 모든 필드
class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True) # nested serializer
    comments = CommentSerializer(many=True, read_only=True) # nested serializer
    # many=True 옵션은 여러 개의 댓글을 배열로 직렬화할 때 사용

    class Meta:
        model = Post
        fields = ("id", "title", "body", "image", "profile", "likes", "published_date", "category", "tags", "summary", "comments")

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
