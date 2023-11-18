from django.shortcuts import render
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
