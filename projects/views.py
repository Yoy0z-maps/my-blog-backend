from django.shortcuts import render
from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer, ProjectCreateSerializer
from users.models import Profile
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return ProjectSerializer
        return ProjectCreateSerializer
    
    def perform_create(self, serializer):
        print(f"🔍 요청된 사용자: {self.request.user}")  # 디버깅
        print(f"🔍 사용자 인증 여부: {self.request.user.is_authenticated}")  # 인증 상태 확인

        profile = Profile.objects.get(user=self.request.user)
        serializer.save(author=self.request.user, profile=profile)


