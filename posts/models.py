from django.db import models
from users.models import User
from users.models import Profile
from django.utils import timezone
import uuid
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    tags = ArrayField(models.CharField(max_length=128))
    summary = models.TextField(null=True, blank=True)
    body = models.TextField() # Json을 Stringfy 할 거임 => 실제로는 TipTapEditor Json Object가 Stringfy됨
    image = models.ImageField(upload_to='posts/', default='default.jpg')
    likes = models.IntegerField(default=0)
    published_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=128, default='default')
    views = models.PositiveIntegerField(default=0)

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nickname = models.CharField(max_length=128)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
