from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    #newUser =djangoModel.Relationship(djangoUserObj, ....)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #directory of pictures uploaded. 

    #Without this, the profile will only return profile object
    def __str__(self):
        return f'{self.user.username} Profile'
        #it will print the username and the profile
       
    #For resizing.... but if u are using aws s3 for storage, it won't work with resizing    
    #def save(self, *args, **kawrgs):
        #super().save()

        #img = Image.open(self.image.path)

        #if img.height > 300 or img.width > 300:
            #output_size = (300, 300)
            #img.thumbnail(output_size)
            #img.save(self.image.path)