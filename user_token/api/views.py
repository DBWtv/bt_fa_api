from rest_framework import views
from rest_framework.response import Response
from .serializers import TokenSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class TokenView(views.APIView):
    serializer_class = TokenSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get(self, request):
        token = request.user.chat_token
        if token.token is None:
            token.generate_token()
        ser = self.serializer_class(token)
        return Response(ser.data, status=200)
