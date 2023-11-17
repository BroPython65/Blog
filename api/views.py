from django.shortcuts import render
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import status

# Create your views here.

class blog_list(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class blog_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer