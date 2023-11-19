from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    host = models.ForeignKey('auth.User', related_name='blogs', null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title