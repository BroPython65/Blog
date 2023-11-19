from django.shortcuts import render
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer, UserSerializer
from rest_framework import status
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User


# Create your views here.

class blog_list(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)

class blog_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer