from rest_framework import views
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.shortcuts import redirect

class RigestrationView(views.APIView):
    serializer_class = CustomUserSerializer

    def post(self, request):
        from_site = request.data.get('from_site', False)
        ser = self.serializer_class(data=request.data)
        if ser.is_valid(raise_exception=True):
            user = ser.create(ser.validated_data)
        if from_site:
            login(request, user)
            return Response({'info': 'success'}, status=200)
        return Response({'info': 'success'}, status=200)


class LoginView(views.APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):

        user = authenticate(
            request,
            username=request.data.get('login'),
            password=request.data.get('password')
        )

        if request.data.get('from_site', False):
            login(request, user)
            return Response({"message": "Authentication successful"})

        if user is not None:
            token = Token.objects.get_or_create(user=user)
            return Response({"message": "Authentication successful", "token": token[0].key})
        else:
            return Response({"error": "Invalid credentials"}, status=400)

@api_view(['GET'])
def logout_view(request):
    logout(request)
    return Response({'info': 'success'}, status=200)