from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from first.models import Car


class CarlistCreateView(APIView):
    def get(self,*args,**kwargs):
        cars = Car.objects.all()
        res=[model_to_dict(car) for car in cars]
        return Response(res,status=status.HTTP_200_OK)

    def post(self,*args,**kwargs):
        data=self.request.data
        car=Car.objects.create(**data)
        car_dict=model_to_dict(car)
        return Response(car_dict,status=status.HTTP_201_CREATED)



class CarRetrieveUpdateDestroyView(APIView):
    def get(self,*args,**kwargs):
        pk=kwargs['pk']
        try:
            car=Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response('Fuck You')
        return Response(model_to_dict(car),status=status.HTTP_200_OK)
    def put(self,*args,**kwargs):
        pk=kwargs['pk']
        data=self.request.data
        try:
            car=Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response('not found')
        car.brand=data['brand']
        car.price=data['price']
        car.year=data['year']
        car.save()
        return Response(model_to_dict(car),status=status.HTTP_200_OK)
    def delete(self,*args,**kwargs):
        pk=kwargs['pk']
        try:
            car=Car.objects.get(pk=pk).delete()
        except Car.DoesNotExist:
            return Response('not found')
        return Response(status=status.HTTP_204_NO_CONTENT)


