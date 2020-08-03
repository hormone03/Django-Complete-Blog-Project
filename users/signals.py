from django.db.models.signals import post_save
from django.contrib.auth.models import User #it will send the signal
from django.dispatch import receiver #will rcv the signal and perform some action
from .models import Profile #the profile will create


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()