from django.contrib import admin
from .models import Post

#register the Post here so that any logged admin will see the posts
#user and in admin by default
admin.site.register(Post)