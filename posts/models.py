from django.db import models
from users.models import User
from users.models import Profile
from django.utils import timezone
import uuid
# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    tags = models.CharField(max_length=128)
    body = models.TextField()
    image = models.ImageField(upload_to='posts/', default='default.jpg')
    likes = models.IntegerField(default=0)
    published_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=128, default='default')