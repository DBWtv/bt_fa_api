from tg_connection.models import TelegramUser
from rest_framework.response import Response
from user_messages.tg_bot_commands.commands import send_message
from user_messages.models import MessageLog


def validate(request):
    if request.data.get('message') == '':
        return Response({'info': 'message cannot be empty'}, status=400)
    instance = get_chat_id(request)
    if isinstance(instance, Response):
        return instance
    message = {
        'first_name': instance.first_name,
        'message': request.data['message'],
    }
    register_message(request)
    return message, instance.user_id
    
def send(message, user_id):
    send_message(message, user_id)


def get_chat_id(request):
    try:
        return TelegramUser.objects.get(user_site=request.user)
    except:
        return Response({'info': 'you should register token'}, status=400)


def register_message(request):
    MessageLog.objects.create(
        user = request.user,
        message = request.data['message'],
    )
    

def get_all_messages_for_user(request):
    messages = MessageLog.objects.filter(user=request.user).order_by('-date')
    return messages