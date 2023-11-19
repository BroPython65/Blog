from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.all_blog_display, name='all_blog_display'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout')
]