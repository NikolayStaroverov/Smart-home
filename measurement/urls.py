from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import SensorsView, SensorView, MeasureViewset

r = DefaultRouter()
r.register('temp',MeasureViewset)

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensor/<pk>/', SensorView.as_view()),
]+r.urls
