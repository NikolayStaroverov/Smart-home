from django.urls import path
from .views import SensorsView

urlpatterns = [
    path('get/', SensorsView),
    # path('get_1/<pk>/', SensorView_1.as_view())
]
