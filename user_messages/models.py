from django.db import models
from CustomUser.models import CustomUser

class MessageLog(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='messages',
    )
    message = models.TextField()
    date = models.DateTimeField(
        auto_now_add=True,
    )
    
    def __str__(self):
        return f'{self.user} - {self.date}'
    
    class Meta:
        ordering = ['-date']

