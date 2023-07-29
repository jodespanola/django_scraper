from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import views, status
from rest_framework.parsers import JSONParser
from . import serializers, models
from json import JSONDecodeError

class DataAPIView(views.APIView):

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return serializers.DataSerializer(*args, **kwargs)

    def get(self, request) -> Response:
        data = models.data.objects.all()
        serializer = serializers.DataSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request) -> Response:
        try:
            serializer = serializers.DataSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({'result': 'error', 'message': 'JSON decoding error'}, status=400)
