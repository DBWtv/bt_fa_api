from tg_connection.models import TelegramUser
from django.db.utils import IntegrityError


def register(user, request):
    request.data['message'].pop('message')
    try:
        TelegramUser.objects.create(
            **request.data['message'],
            user_site=user,
        )
        return {'info': 'success'}, 200
    except IntegrityError:
        return {'info': 'User already exists'}, 400
    
