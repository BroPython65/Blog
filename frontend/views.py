from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from api.models import Blog
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import BlogPostForm
from django.urls import reverse
from django.db.models import Count

# Create your views here.

#This will display all blog post
def all_blog_display(request):
    user = request.user
    return render(request, 'frontend/blog.html', {'user':user})

#Create post here
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Create the blog post
        new_post = Blog.objects.create(title=title, content=content, host=request.user)
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

#authentication
def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            pass
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            pass
    context = {'page':page}
    return render(request, 'frontend/login_register.html', context)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def register_page(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
           user = form.save(commit=False)
           user.username = user.username.lower()
           user.save()
           login(request, user)
           return redirect('/')
        else:
           pass

    context = {'form':form}
    return render(request, 'frontend/login_register.html', context)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def logout_page(request):
    logout(request)
    return redirect('/')
#end authentication


def user_detail(request, pk):
    user = get_object_or_404(User, username=pk)
    blogs = Blog.objects.filter(host=user).annotate(likes_count=Count('likes'))
    return render(request, 'frontend/user.html', {'blogs': blogs, 'user': user})


#update from user url
def update_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    user = blog.host
    id = pk
    if request.method == 'PUT':
        title = request.POST.get('title')
        content = request.POST.get('content')
        blog.title = title
        blog.content = content
        blog.save()
    return render(request, 'frontend/update.html', {'blog':blog, 'id':id, 'user':user})

