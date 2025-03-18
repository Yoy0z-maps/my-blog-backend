from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import uuid

# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # primary_key를 Userdml pk로 설정하여 통합적으로 관리 의
    nickname = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    image = models.ImageField(upload_to='profile/', default='default.jpg')

    # 프로필 데이터를 문자열로 표현
    def __str__(self):
        return self.nickname

# User모델이 post_save 이벤트를 발생시켰을 때, 해당 유저 인스턴스와 연관되는 프로필 데이터를 생성
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
