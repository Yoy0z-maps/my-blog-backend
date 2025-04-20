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
from .models import Comment
from .serializers import CommentSerializer, CommentCreateSerializer

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
        if self.action in ['list', 'retrieve']:
            return PostSerializer
        return PostCreateSerializer
    
    def perform_create(self, serializer):
        print(f"🔍 요청된 사용자: {self.request.user}") 
        print(f"🔍 사용자 인증 여부: {self.request.user.is_authenticated}") 

        profile = Profile.objects.get(user=self.request.user)
        serializer.save(author=self.request.user, profile=profile)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        session_key = f"viewed_post_{instance.pk}"
        if not request.session.get(session_key):
            instance.views += 1
            instance.save(update_fields=["views"])
            request.session[session_key] = True

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='like', permission_classes=[permissions.AllowAny])
    def like_post(self, request, pk=None):
        try:
            post = self.get_object()

            if post.likes is None:
                post.likes = 0

            post.likes += 1
            post.save()

            return Response({'message': 'Liked!', 'likes': post.likes}, status=status.HTTP_200_OK)
        except Exception as e:
            print("🔥 like_post 에러:", e)
            return Response({'error': 'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.action in 'list' or 'retrieve':
            return CommentSerializer
        return CommentCreateSerializer
    
    def perform_create(self, serializer):
        serializer.save()
        