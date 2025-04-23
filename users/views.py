from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from .permissions import CustomReadOnly
# Create your views here.

# 회원가입을 위한 API 엔드포인트를 만들 때, CreateAPIView를 사용하면 POST 요청만 처리할 수 있도록 제한됨
# CreateAPIView는 DRFD의 GenericAPIView 중 하나로 새로운 객체(모델 인스턴스)를 생성하는 데 특화된 API View, 즉 POST 요청을 통해 객체를 생성하는 기능만 제공
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# 로그인 구현
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data # validate의 반환 값인 Token을 받아옴
        response = Response({
            "token": token.get('token'),
            "uuid": token.get('uuid')
        }, status=status.HTTP_200_OK)

        response.set_cookie(key="token", value=token.get('token'), httponly=True, path="/", secure=True, samesite='Lax', domain=".yoy0z-maps.com", max_age=60*60*24)
        response.set_cookie(key="uuid", value=token.get('uuid'), httponly=True, path="/", secure=True, samesite='Lax', domain=".yoy0z-maps.com", max_age=60*60*24)
        return response
    
# 프로필 조회
from .models import Profile

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [CustomReadOnly]
    
    