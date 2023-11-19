from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Blog
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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