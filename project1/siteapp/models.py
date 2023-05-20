from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to = "images/", null=True, blank=True)
    
    
    def __str__(self):
        return str(self.title)  
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    
# class Blog(models.Model):
#     text=models.TextField()