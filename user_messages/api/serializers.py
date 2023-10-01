from rest_framework import serializers
from user_messages.models import MessageLog


class MessageSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S")
    
    class Meta:
        model = MessageLog
        exclude = ['user']
