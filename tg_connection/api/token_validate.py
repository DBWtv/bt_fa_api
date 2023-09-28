from rest_framework.response import Response
from django.conf import settings
from user_token.models import TokenTgChat
import re


def validate(request, token):
    if token != settings.TG_BOT_API_TOKEN:
        return Response({'info': 'invalid token'}, status=405)

    if not validate_token(request.data['message']['message']):
        return Response({'info': 'Token is wrong'}, status=400)
    
    user = TokenTgChat.objects.get(
        token=request.data['message']['message']).user
    
    if check_register(user):
        return Response({'info': 'Token already exists'}, status=400)
    
    return user


def validate_token(token) -> bool:
    if re.match(r'^[0-9a-fA-F]{64}$', token):
        return True
    return False


def check_register(user) -> bool:
    try:
        user.telegram_user
        return True
    except:
        return False
