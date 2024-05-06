from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile

#whenever a new user is created automatically his/her profile will get updated with default parameter
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs) -> None:
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs) -> None:
    instance.profile.save()