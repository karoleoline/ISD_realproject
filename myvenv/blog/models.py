#Defining creation setting for post and where you create the database objects and query.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#class to for Posts. Defining restriction of post and create your post here
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # conncected to the User model using the Foreign Key
    
    #show us  what is title of post
    def __str__(self):
        return self.title
    
# to find the url to any specific instance of a post and need primary key.
# for creating new post. get the url of particular route to do this use reverse
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
