from rest_framework import status
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializer import AutoparkSerializer
from apps.first.serializers import CarSerializer


class AutoParksView(ListCreateAPIView):
    serializer_class =AutoparkSerializer
    queryset = AutoParkModel.objects.all()

# Create your views here.
class AutoparkAddCarView(CreateAPIView):
    queryset = AutoParkModel.objects.all()
    def post(self, request, *args, **kwargs):
        auto_park=self.get_object()
        data=self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        ap_serializer=AutoparkSerializer(auto_park)
        return Response(ap_serializer.data, status=status.HTTP_201_CREATED)
