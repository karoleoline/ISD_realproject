from django.conf.urls import url
from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView)


urlpatterns = [
    path('register/',views.register, name='register'),
    path('profile/',views.profile, name='profile'),
    path('profile/account/', views.edit_profile, name='editprofile'),
    path('profile/password/',PasswordResetView.as_view(), name='change-profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),

    url(r'^reset-password/$', PasswordResetView, {'template_name': 'accounts/reset_password.html', 'post_reset_redirect': 'accounts:password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'}, name='reset_password'),

    url(r'^reset-password/done/$', PasswordResetDoneView, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView, {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),

    url(r'^reset-password/complete/$', PasswordResetCompleteView,{'template_name': 'accounts/reset_password_complete.html'}, name='password_reset_complete')

]
