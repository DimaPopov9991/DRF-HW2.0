from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.first.models import Car


class CarSerializer(serializers.ModelSerializer):
   class Meta:
       model = Car
       fields = ('id','brand','year','price','create_at','updated_at','body_type','auto_park')

   def validate(self, data):
      if data['price']== data['year']:
          raise ValidationError('Price cannot be the same')


      return data



