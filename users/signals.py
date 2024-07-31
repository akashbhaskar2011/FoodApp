from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save,sender=User)
def build_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
        # this is used to sace that was done separately with the other method
        

# @receiver(post_save,sender=User)
# def save_profile(sender,instance, **kwargs):
#     instance.profile.save()
# this can be done along with tthe adding single line in the build profile 