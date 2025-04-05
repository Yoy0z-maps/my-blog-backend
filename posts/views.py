from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer, PostCreateSerializer
from .permissions import CustomReadOnly
from users.models import Profile
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import permissions
# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-published_date')
    permission_classes = [CustomReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author','category']

    # def list(self, request, *args, **kwargs):
    #     print(f"🔍 요청된 사용자: {request.user}")  # 사용자 정보 출력
    #     print(f"🔍 인증 여부: {request.user.is_authenticated}")  # 인증 상태 출력
        
    #     if not request.user.is_authenticated:
    #         return Response({"error": "인증 실패 (403) - request.user가 비어 있음"}, status=status.HTTP_403_FORBIDDEN)

    #     return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return PostSerializer
        return PostCreateSerializer
    
    def perform_create(self, serializer):
        print(f"🔍 요청된 사용자: {self.request.user}")  # 디버깅
        print(f"🔍 사용자 인증 여부: {self.request.user.is_authenticated}")  # 인증 상태 확인

        profile = Profile.objects.get(user=self.request.user)
        serializer.save(author=self.request.user, profile=profile)

    @action(detail=True, methods=['post'], url_path='like', permission_classes=[permissions.AllowAny])
    def like_post(self, request, pk=None):
        try:
            post = self.get_object()
            post.likes += 1
            post.save()
            return Response({'message': 'Liked!', 'likes': post.likes}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)