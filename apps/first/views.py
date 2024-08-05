from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)

from apps.first.filter import carfilter
from apps.first.models import Car
from apps.first.serializers import CarSerializer


class CarlistCreateView(GenericAPIView, CreateModelMixin, ListModelMixin):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


    def get_queryset(self):
        return carfilter(self.request.query_params)


    def get(self, request, *args, **kwargs):

        return super().list(request, *args, **kwargs)



    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


# def get (self,*args,**kwargs):
    #     qs=Car.objects.all()
    #     ser=CarSerializer(qs,many=True)
    #     return Response(ser.data,status=status.HTTP_200_OK)
    #
    #
    # def post(self,*args,**kwargs):
    #     data=self.request.data
    #     serializer=CarSerializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response(serializer.data,status=status.HTTP_201_CREATED)






class CarRetrieveUpdateDestroyView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    serializer_class = CarSerializer
    queryset = Car.objects.all()




    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    # def get(self,*args,**kwargs):
    #     # pk=kwargs['pk']
    #     # try:
    #     #     car=Car.objects.get(pk=pk)
    #     # except Car.DoesNotExist:
    #     #     return Response('Fuck You')
    #
    #     car= self.get_object()
    #     serializer=CarSerializer(car)
    #     return Response(serializer.data,status=status.HTTP_200_OK)
    # def put(self,*args,**kwargs):
    #     # pk=kwargs['pk']
    #     data=self.request.data
    #     # try:
    #     #     car=Car.objects.get(pk=pk)
    #     # except Car.DoesNotExist:
    #     #     return Response('not found')
    #     car= self.get_object()
    #     serializer=CarSerializer(car,data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response(serializer.data,status=status.HTTP_200_OK)
    #
    #
    # def patch(self,*args,**kwargs):
    #     pk=kwargs['pk']
    #     data=self.request.data
    #     try:
    #         car=Car.objects.get(pk=pk)
    #     except Car.DoesNotExist:
    #         return Response('not found')
    #     serializer=CarSerializer(car,data=data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response(serializer.data,status=status.HTTP_200_OK)
    # def delete(self,*args,**kwargs):
    #     # pk=kwargs['pk']
    #     # try:
    #     #     car=Car.objects.get(pk=pk).delete()
    #     # except Car.DoesNotExist:
    #     #     return
    #     self.get_object().delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)





