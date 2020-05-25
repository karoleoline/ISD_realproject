from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import UserRegisterForm, EditProfileForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hey {username}! Welcome to the Neighborhood:)')
            return redirect ('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'login/register.html', {'form' : form})

def profile(request):
    #context = {'user': request.user}
    return render(request, 'login/profile.html')

def editprofile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect ('profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'login/edit_profile.html', args)
