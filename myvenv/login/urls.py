from django.conf.urls import url
from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView)


urlpatterns = [
    path('register/',views.register, name='register'),
    #path('profile/',views.profile, name='profile'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    #path('profile/',views.profile, name='profile'),
    path('profile/account/', views.edit_profile, name='editprofile'),
    path('profile/password/',PasswordResetView.as_view(), name='change-profile'),


]
