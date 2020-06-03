from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, UserProfileUpdateForm
from django.http import HttpResponse, Http404

#profile view, login required, only the own profile can be edited
@login_required
def profile(request, username):

    # If no such user exists raise 404
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404
    # if the user visits his own profile (thus username == request.username) he can edit it, else not
    if username == request.user.username:

        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = UserProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('profile')

        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = UserProfileUpdateForm(instance=request.user.userprofile)

            context = {
            'u_form': u_form,
            'p_form': p_form
        }

        return render(request, 'login/edit_profile.html', context)

    else:
        args = {
            'user':  user
            }

        return render(request, 'login/profile.html', args)


#register as User
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user_firstname = form.cleaned_data.get('first_name')
            messages.success(request, f'Hey { user_firstname }! Welcome to the Neighborhood:)')
            return redirect ('login')
    else:
        form = UserRegisterForm()
    return render(request, 'login/register.html', {'form' : form})

#change password via getting an email
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
        return render(request, 'login/reset_password.html', args)
