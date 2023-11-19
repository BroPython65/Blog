from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blog_display, name='all_blog_display'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>', views.edit, name='edit')
]