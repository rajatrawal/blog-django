from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=5000)
    author = models.CharField(max_length=40)
    time_stamp = models.DateTimeField(blank=True)
    views = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    Comment = models.TextField(max_length=5000, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(default=now)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.Comment[0:15]
