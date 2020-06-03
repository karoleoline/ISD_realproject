from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Post
from django.core.mail import send_mail
from django.views.generic import (DetailView,ListView,CreateView,UpdateView,DeleteView)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#home view showing all the posts
def home(request):

    post_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(title__icontains=query)
    paginator = Paginator(post_list, 8)  # Show 8 posts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/home.html', {'posts': posts})

#view of all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

#detail view of a post
class PostDetailView(DetailView):
    model = Post
    template = 'post_detail.html'

#create a post
class PostCreateView(LoginRequiredMixin, CreateView):
		model = Post
		fields = ['title', 'content']

		def form_valid(self, form):
			form.instance.author = self.request.user
			return super().form_valid(form)

#update a post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#view of the about page
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

#view of the contact page
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
