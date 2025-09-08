from rest_framework import permissions

'''
전체 동작 흐름:
1. 요청 들어옴 → has_permission 실행
2. 인증 확인 → 인증되지 않으면 401 에러
3. 인증 통과 → has_object_permission 실행
4. 객체 권한 확인:
    - GET: 모든 인증된 사용자 허용
    - PATCH/PUT: 소유자만 허용
'''


class CustomReadOnly(permissions.BasePermission):
    # 뷰에 대한 전체적인 접근 권한
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
        # request.user: 요청한 사용자가 존재하는지
        # request.user.is_authenticated: 요청한 사용자가 인증되었는지

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # SAFE_METHODS는 GET 같이 데이터에 영향을 안 주는 메서드
            return True
        return obj.user == request.user