from rest_framework import serializers
from .models import Project
from users.serializers import ProfileSerializer
class ProjectSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True) # nested serializer

    class Meta:
        model = Project
        fields = ("id", "profile","title", "content", "link", "tags", "thumbnail_image",  "created_at")
        
class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("title", "content", "link", "tags", "thumbnail_image")