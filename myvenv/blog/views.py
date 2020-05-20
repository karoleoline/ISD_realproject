from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.core.mail import send_mail



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

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
			['aksoy.dipioglu@uni.li'], # To Email
			fail_silently = False
			)

		return render(request, 'blog/contact.html', {'message_name': message_name})

	else:
		return render(request, 'blog/contact.html', {})
