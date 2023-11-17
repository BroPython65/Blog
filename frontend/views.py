from django.shortcuts import render

# Create your views here.

#This will display all blog in fetch api
def all_blog_display(request):
    return render(request, 'frontend/blog.html', {})