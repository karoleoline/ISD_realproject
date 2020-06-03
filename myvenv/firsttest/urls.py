"""firsttest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from login import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('login.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login/logout.html'), name='logout'),

    url(r'^reset-password/$', auth_views.PasswordResetView.as_view(), {'template_name': 'login/reset_password.html', 'post_reset_redirect': 'login:password_reset_done', 'email_template_name': 'login/reset_password_email.html'}, name='reset_password'),

    url(r'^reset-password/done/$', auth_views.PasswordResetDoneView.as_view(), {'template_name': 'login/reset_password_done.html'}, name='password_reset_done'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(), {'template_name': 'login/reset_password_confirm.html', 'post_reset_redirect': 'login:password_reset_complete'}, name='password_reset_confirm'),

    url(r'^reset-password/complete/$', auth_views.PasswordResetCompleteView.as_view(),{'template_name': 'login/reset_password_complete.html'}, name='password_reset_complete')

]



if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
