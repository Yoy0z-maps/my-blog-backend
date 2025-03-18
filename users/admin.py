from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

# admin.StackedInline울 상속 받고, Profile모델을 User에 인라인으로 추가
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

# UserAdmin을 상속 받고 User 모델의 관리자 인터페이스를 커스터마이징
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    
# 기존 제공되는 User 모델의 관리자 등록을 해제
admin.site.unregister(User) 
# User 모델을 커스터마이징된 UserAdmin으로 등록
admin.site.register(User, UserAdmin)
