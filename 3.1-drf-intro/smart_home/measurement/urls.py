from django.urls import path

from measurement.views import SensorView, SensorRetrieveView, MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorRetrieveView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
