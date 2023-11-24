from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User



class BlogSerializer(serializers.ModelSerializer):
    host = serializers.ReadOnlyField(source='host.username')
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'host', 'title', 'content', 'likes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()
    
class UserSerializer(serializers.ModelSerializer):
    blogs = serializers.PrimaryKeyRelatedField(many=True, queryset=Blog.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'blogs']