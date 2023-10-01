from rest_framework.views import APIView
from rest_framework.response import Response
from .services import validate, send, get_all_messages_for_user
# import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from .serializers import MessageSerializer



class MessageView(APIView):
    @csrf_exempt
    def post(self, request):
        
        send(*validate(request))
        
        return Response({'info': 'success'}, status=200)


class MessageHistory(APIView):
    
    def get(self, request):
        ser = MessageSerializer(get_all_messages_for_user(request), many=True)
        return Response(ser.data, status=200)