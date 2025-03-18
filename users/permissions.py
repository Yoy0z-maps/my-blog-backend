from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print("============================")
        print(obj.user)
        print(request.user)
        print("============================")
        if request.method in permissions.SAFE_METHODS: # SAFE_METHODS는 GET 같이 데이터에 영향을 안 주는 메서드
            print("safe method")
            return True
        print("access denied")
        return obj.user == request.user