from django.db import models
import uuid
from django.utils import timezone
from users.models import User
from users.models import Profile
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    thumbnail_image = models.ImageField(upload_to='projects/', default='default.jpg')
    title = models.TextField() # Json을 Stringfy 할 거임 => {ko: "", en: ""}
    content = models.TextField() # Json을 Stringfy 할 거임 => {ko: "", en: ""}
    github_link = models.URLField(max_length=200, null=True, blank=True)
    figma_link = models.URLField(max_length=200, null=True, blank=True)
    appstore_link = models.URLField(max_length=200, null=True, blank=True)
    playstore_link = models.URLField(max_length=200, null=True, blank=True)
    web_link = models.URLField(max_length=200, null=True, blank=True)
    project_date = models.DateField(null=True, blank=True)
    tags = ArrayField(models.CharField(max_length=128))

    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/')
    uploaded_at = models.DateTimeField(auto_now_add=True)