from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import UserRegisterForm#, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, UserProfileUpdateForm



#profile view, login required
@login_required
def profile(request, username):
    # If no such user exists raise 404
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404

    # Flag that determines if we should show editable elements in template
    editable = False
    # Handling non authenticated user for obvious reasons
    if request.user.is_authenticated and request.user == user:
        editable = True


    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated successfully')
            return redirect ('profile', username=username)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.userprofile)

    context = {
    'u_form': u_form,
    'p_form': p_form
    }

    return render(request, 'login/profile.html', context)

#register

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save(request)
            username = form.cleaned_data.get('username')
            user_firstname = form.cleaned_data.get('first_name')
            messages.success(request, f'Hey { user_firstname }! Welcome to the Neighborhood:)')
            return redirect ('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'login/register.html', {'form' : form})

#edit profile
"""
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect ('profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'login/edit_profile.html', args)
"""


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('login:view_profile'))
        else:
            return redirect(reverse('login:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'login/change_password.html', args)

def view_profile(request, username):
    if pk:
        user = User.objects.get(username=username)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'login/profile.html', args)
