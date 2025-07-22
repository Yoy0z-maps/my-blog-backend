from rest_framework import serializers
from .models import Project, ProjectImage
from users.serializers import ProfileSerializer

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image', 'uploaded_at']

class ProjectSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    images = ProjectImageSerializer(many=True, read_only=True)  # related_name='images' 사용

    class Meta:
        model = Project
        fields = ("id", "profile", "title", "content", "github_link", "figma_link", "appstore_link", "playstore_link", "web_link", "tags", "created_at", "images")

class ProjectCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )

    class Meta:
        model = Project
        fields = ("title", "content", "github_link", "figma_link", "appstore_link", "playstore_link", "web_link", "tags", "images")

    def create(self, validated_data):
        images = validated_data.pop('images', [])
        project = Project.objects.create(**validated_data)
        for image in images:
            ProjectImage.objects.create(project=project, image=image)
        return project