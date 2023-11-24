from django.shortcuts import render
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer, UserSerializer
from rest_framework import status
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect


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

def like_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    user = request.user

    liked = blog.like(user)
    like_count = blog.likes.count()

    response_data = {
        'liked': liked,
        'like_count': like_count,
    }

    return JsonResponse(response_data)