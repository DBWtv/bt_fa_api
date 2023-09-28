from rest_framework.views import APIView
from rest_framework.response import Response
from .token_validate import validate
from .register_user import register


class TgBotView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, token):
        instance = validate(request, token)

        if isinstance(instance, Response):
            return instance

        return Response(*register(instance, request))
