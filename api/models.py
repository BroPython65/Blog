from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=999999)

    def __str__(self):
        return self.title