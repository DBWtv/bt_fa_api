from rest_framework.views import APIView
from rest_framework.response import Response
from .services import validate, send


class MessageView(APIView):
    def post(self, request):
        
        send(*validate(request))
        
        return Response({'info': 'success'}, status=200)
