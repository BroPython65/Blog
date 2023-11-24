from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    host = models.ForeignKey('auth.User', related_name='blogs', null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_blogs', blank=True)

    def __str__(self):
        return self.title
    
    def like(self, user):
        if user not in self.likes.all():
            self.likes.add(user)
            return True  # Indicate that the blog was liked
        else:
            self.likes.remove(user)
            return False  # Indicate that the like was removed
