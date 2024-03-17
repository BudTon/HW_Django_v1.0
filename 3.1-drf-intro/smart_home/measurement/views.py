from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Sensor, SensorDetail
from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(f'the data is recorded \n{request.data}')
        else:
            return HttpResponse(f'data recording error \n{request.data}')



class SensorRetrieveView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(id=pk)
        key_request = request.data
        for key in key_request:
            if key == 'description':
                sensor.description = request.data[f'{key}']
                sensor.save()
            elif key == 'name':
                sensor.name = request.data[f'{key}']
                sensor.save()
            else:
                return HttpResponse(f'the data has been changed to ERROR: \n{request.data}')
        return HttpResponse(f'the data has been changed to: \n{request.data}')


class MeasurementView(ListCreateAPIView):
    queryset = SensorDetail.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(f'the data is recorded \n{request.data}')
        else:
            return HttpResponse(f'data recording error \n{request.data}')
