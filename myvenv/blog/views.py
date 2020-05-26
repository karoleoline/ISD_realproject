from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.core.mail import send_mail
from django.views.generic import (DetailView,ListView)



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template = 'post_detail.html'

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# send an email
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from email
			['isd.project2020@gmail.com'], # To Email
			fail_silently = False
			)

		return render(request, 'blog/contact.html', {'message_name': message_name})

	else:
		return render(request, 'blog/contact.html', {})
