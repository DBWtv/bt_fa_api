from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import TokenTgChat


@receiver(post_save, sender=get_user_model())
def create_token_instance(sender, instance, created, **kwargs):
    if created:
        TokenTgChat.objects.create(user=instance)
