from django.db import models
from CustomUser.models import CustomUser

class TelegramUser(models.Model):
    user_id = models.IntegerField(
        unique=True,
    )
    username = models.CharField(
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        max_length=255,
        null=True
    )
    last_name = models.CharField(
        max_length=255,
        null=True
    )
    user_site = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='telegram_user',
    )
    
