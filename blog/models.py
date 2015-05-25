from django.db import models
from jpype import *

from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text=models.TextField()

    created_date= models.DateTimeField(default=timezone.now)
    publish_date= models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)
    
    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text

    
