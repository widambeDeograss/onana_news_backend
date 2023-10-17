from django.db import models
import uuid
from user_management.models import User


# Create your models here.
class NewsAgents(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    profile = models.ImageField(upload_to="uploads/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class NewsArticles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    provider = models.CharField(max_length=100)
    tittle = models.CharField(max_length=400)
    pic1 = models.ImageField(upload_to="uploads/", null=True, blank=True)
    subtitle = models.CharField(max_length=900)
    content = models.TextField()
    pic2 = models.ImageField(upload_to="uploads/", null=True, blank=True)
    sub_content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.tittle


class ArticleComments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(NewsArticles, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)



