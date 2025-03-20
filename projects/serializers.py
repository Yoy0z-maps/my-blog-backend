from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "title", "content", "link", "tags", "thumbnail_image", "profile", "published_date")
        
class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("title", "content", "link", "tags", "thumbnail_image")