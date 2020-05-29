from django.urls import path
from . import views
from .views import (PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView)


urlpatterns = [
    path('', views.home, name='blog-home'),

    path('about/', views.about, name='blog-about'),
    # path('about/', PostListView.as_view(), name='blog-about'),

    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('contact/', views.contact, name='blog-contact'),
    # path('<int:pk>', views.PostDetailView, name='post-detail'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
