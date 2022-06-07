from rest_framework.views import APIView
from .serializers import AdocaoSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .email_service import send_confirmation_email


class AdocaoList(APIView):
    def post(self, request, format=None):
        serializer = AdocaoSerializer(data=request.data)
        if serializer.is_valid():
            adocao = serializer.save()
            send_confirmation_email(adocao)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(
            {
                "errors": serializer.errors,
                "message": "Houveram erros de validação",
            },
            status=HTTP_400_BAD_REQUEST,
        )
