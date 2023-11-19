from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
    host = serializers.ReadOnlyField(source='host.username')

    class Meta:
        model = Blog
        fields = ['id', 'host', 'title', 'content']

    
class UserSerializer(serializers.ModelSerializer):
    blogs = serializers.PrimaryKeyRelatedField(many=True, queryset=Blog.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'blogs']