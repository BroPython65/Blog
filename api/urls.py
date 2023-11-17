from django.urls import path
from .views import blog_detail, blog_list

urlpatterns = [
    path('blog-list', blog_list.as_view() , name='blog-list'),
    path('blog-detail/<int:pk>', blog_detail.as_view() , name='blog-deatil')
]