from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Blog

# Create your views here.

#This will display all blog post
def all_blog_display(request):
    return render(request, 'frontend/blog.html', {})

#Create post here
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Create the blog post
        new_post = Blog.objects.create(title=title, content=content)
    return render(request, 'frontend/create.html')

#Update function
def edit(request, pk):
    blog = Blog.objects.get(id=pk)
    id = pk
    if request.method == 'PUT':
        # Handle form submission and update data
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Update the blog object with new data
        blog.title = title
        blog.content = content
        blog.save()
    return render(request, 'frontend/edit.html', {'blog':blog, 'id':id})
