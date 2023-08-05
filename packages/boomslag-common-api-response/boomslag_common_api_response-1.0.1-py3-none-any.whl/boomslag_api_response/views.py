from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import APIResponseSerializer

class BaseAPIView(APIView):
    def send_response(self, data=None, status=status.HTTP_200_OK):
        serializer = APIResponseSerializer({
            'success': True,
            'data': data
        })
        return Response(serializer.data, status=status)

    def send_error(self, error, status=status.HTTP_400_BAD_REQUEST):
        serializer = APIResponseSerializer({
            'success': False,
            'error': error
        })
        return Response(serializer.data, status=status)