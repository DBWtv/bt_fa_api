from django.db import models
from CustomUser.models import CustomUser
import secrets

class TokenTgChat(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='chat_token',
    )
    token = models.CharField(
        max_length=255,
        unique=True,
        null=True,
    )

    def __str__(self):
        if self.token is None:
            return 'None'
        return self.token
    
    def generate_token(self):
        token = secrets.token_hex(32)
        try:
            if TokenTgChat.objects.get(token = token) is not None:
                self.generate_token()
        except TokenTgChat.DoesNotExist:
            self.token = token
            self.save()
        return self.token
