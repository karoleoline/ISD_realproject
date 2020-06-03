# urls.py is responsible for the routing and requests, i.e., if a user types in a URL, this file forwards the request to
# the appropriate function in the views.py.

from django.urls import path
from . import views
from .views import (PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView)

#will show us what is inside of url address and what will do
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    
    #pk: primary key. delete update or detail only selected post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('contact/', views.contact, name='blog-contact'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
