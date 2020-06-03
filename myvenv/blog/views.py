# Views access the Models and prepare the data before showing
# write functions here. User's request and response performed here.

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Post
from django.core.mail import send_mail
from django.views.generic import (DetailView,ListView,CreateView,UpdateView,DeleteView)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#home view showing all the posts and settings for home page, home function
def home(request):

    post_list = Post.objects.all() # will show post in DB.

    #Search button.. checking if user enter any word for search or not.
    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(title__icontains=query) # searching according to title
    paginator = Paginator(post_list, 8)  # Show 8 posts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/home.html', {'posts': posts})

#view/listing of all posts,home list view.
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

#detail view of a post and to see only single post
class PostDetailView(DetailView):
    model = Post
    template = 'post_detail.html'

#create a post and Enable user to create new post
class PostCreateView(LoginRequiredMixin, CreateView):
		model = Post
		fields = ['title', 'content']
		
        #Getting current logged in user.Author can create a new post
		def form_valid(self, form):
			form.instance.author = self.request.user #take current user and set for new post
			return super().form_valid(form)

#update a post.only user who logged in and owner of post can update
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

#delete a post.Only user who logged in and owner of post can delete
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' # if we delete post,  we are redirected to homepage

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
	if request.method == "POST": # someone who only fulfill form and do here
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# send an email function from getting library
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from email
			['isd.project2020@gmail.com'], # To Email
			fail_silently = False
			)
        	# someone who only see contact page again after fulfilling form
		return render(request, 'blog/contact.html', {'message_name': message_name})

	else: # someone who only see contact page wihtout doing anything, return the page
		return render(request, 'blog/contact.html', {})
