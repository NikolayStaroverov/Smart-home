# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer


# @api_view(["GET"])
# def SensorsView(request):
#     sensor = Sensor.objects.all()
#     sen = SensorDetailSerializer(sensor,many=True)
#     return Response(sen.data)


# class SensorsView(APIView):
#     def get(self,request):
#         sensor = Sensor.objects.all()
#         sen = SensorDetailSerializer(sensor, many=True)
#         return Response(sen.data)
#
#     def post(self,request):
#         return Response({'status':'OK'})


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self,request):
        return Response({'status':'OK'})


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasureViewset(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
