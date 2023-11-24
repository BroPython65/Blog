from django.urls import path
from .views import blog_detail, blog_list
from . import views

urlpatterns = [
    path('blog-list', blog_list.as_view() , name='blog-list'),
    path('blog-detail/<int:pk>', blog_detail.as_view() , name='blog-deatil'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('blog-detail/<int:blog_id>/like', views.like_blog, name='like_blog')
]