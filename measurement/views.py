# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor
from .serializers import SensorDetailSerializer

@api_view(["GET"])
def SensorsView(request):
    sensor = Sensor.objects.all()
    sen = SensorDetailSerializer(sensor)
    return Response(sen.data)