from rest_framework import serializers
from user_token.models import TokenTgChat


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = TokenTgChat
        fields = ('token', 'user')
        read_only_fields = ('token', 'user')
