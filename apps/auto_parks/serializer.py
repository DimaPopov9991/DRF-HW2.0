from rest_framework import serializers

from apps.auto_parks.models import AutoParkModel
from apps.first.serializers import CarSerializer


class AutoparkSerializer(serializers.ModelSerializer):
    cars=CarSerializer(many=True, read_only=True)
    class Meta:
        model=AutoParkModel
        fields=('id','name','create_at','updated_at','cars')


