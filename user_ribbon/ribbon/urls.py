from django.contrib.auth import views as auth_views
from django.urls import path, include
from ribbon.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    UserPostListView,
    RegisterView
)


urlpatterns = [
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='ribbon/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='ribbon/logout.html'), name='logout'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
]
