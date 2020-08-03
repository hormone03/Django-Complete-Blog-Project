from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post




def home(request):
    context = {
        'posts': Post.objects.all() #Post is from model.py class
    }
    return render(request, 'blog/home.html', context) 


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts' #by default, posts is set to bojectList, but we want to use another variable
    ordering = ['-date_posted']
    paginate_by = 3
    

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts' #by default, posts is set to bojectList, but we want to use another variable
    ordering = ['-date_posted']
    paginate_by = 3
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username')) #getting the username from the url, else return 404
        return Post.objects.filter(author=user).order_by('-date_posted') #get posts from the user




class PostDetailView(DetailView): #will lint to each post by id
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView): # LoginRequiredMixin to ensure inly loggedin user to post
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): #We need to override the form_valid
        form.instance.author = self.request.user #this will set the instance of the form to the current user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #UserPassesTestMixin ensures that u can only edit your own posts
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True #that is allow them to update the post
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) #we pass in the title want to use in the html, not default
                                                                #PS: title in this arg will appear on tab