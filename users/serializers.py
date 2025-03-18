from django.contrib.auth.models import User # User Model
from django.contrib.auth.password_validation import validate_password # Password Validation

from rest_framework import serializers
from rest_framework.authtoken.models import Token # Token Model
from rest_framework.validators import UniqueValidator # Email Conflict Validation

from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())] # Check if email is unique
    )
    password = serializers.CharField(
        write_only=True, # 클라언트로부터 데이터를 받을 때만 사용되고, 응답에는 포함되지 않음
        required=True,
        validators=[validate_password] # Check if password is valid
    )
    password2 = serializers.CharField(write_only=True, required=True)
    
    # 모델 필드(서버에 보낼 데이터 객체)를 직렬화(serialize) 혹은 역직렬화(deserialize)할 때 사용
    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email']
        
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data
    
    # 부모클래스 ModelSerializer의 create 메서드 오버라이딩
    # Python에서는 이름이 같은 메서드면 자동으로 오버라이딩
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user) # 만약 Token을 반환하면 DRF의 직렬화에서 문제가 생길 수 있음 (모델 필드에 포함되지 않음)
        return user
    
# 로그인 구현
from django.contrib.auth import authenticate # Django의 기본 authenticate 함수, DefaultAuthBackend인 TokenAuth방식으로 유저 인증 진행

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
           token = Token.objects.get(user=user) # 토큰 자체는 <class 'rest_framework.authtoken.models.Token'>
           profile = Profile.objects.get(user=user)
           return {
               'token': token.key,
               'uuid': profile.id,
           }
        raise serializers.ValidationError({"error": "Unable to log in with provided credentials."})
    
# 프로필 직렬화
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['nickname', 'position','image']