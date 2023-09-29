from rest_framework.views import APIView
from rest_framework.response import Response
from .services import validate, send
# import csrf_exempt
from django.views.decorators.csrf import csrf_exempt



class MessageView(APIView):
    @csrf_exempt
    def post(self, request):
        
        send(*validate(request))
        
        return Response({'info': 'success'}, status=200)
