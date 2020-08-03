from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #because we want to know who create the post
from django.urls import reverse


class Post(models.Model): #arg: inherit or injection
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #one to many post
                        #CASCADE means once a user deletes its profile, his post should be deleted
    #adding dunder
    def __str__(self): 
        return self.title
    
    #we need to def get_absolute_url, so that it will handle the redirect after posting a blog
    #Otherwise, it will give error, except we define a redirect url
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
        #reverse will return the whole url as a string