from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import Request
from rest_framework import status
from landing.controllers.tilda_callback import TildaCallbackController
from django.core.exceptions import ValidationError


class TildaCallbackApi(APIView):

    @staticmethod
    def get(request: Request) -> Response:
        try:
            TildaCallbackController().save_callback(request.query_params)
            return Response('ok', status=status.HTTP_200_OK)
        except ValidationError as validation_error:
            return Response('%s' % validation_error, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exception:
            return Response('%s' % exception, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
