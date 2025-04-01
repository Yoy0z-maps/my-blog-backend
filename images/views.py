# upload/views.py
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from .models import UploadedImage
from .serializers import UploadedImageSerializer

class ImageUploadView(APIView):
    parser_classes = [MultiPartParser]  # 파일 전송 파서

    def post(self, request, *args, **kwargs):
        serializer = UploadedImageSerializer(data=request.data)

        if serializer.is_valid():
            instance = serializer.save()
            print(request.FILES)               # 👈 실제로 파일 들어왔는지
            print(serializer.errors)          # 👈 is_valid() 실패 시 확인
            print(serializer.validated_data)  # 👈 성공 시 내부 구조
            return Response({
                'id': instance.id,
                'url': instance.image.url  # S3 URL이 자동으로 여기에 들어옴
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)