from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.users.models import ProfileModel

UserModel=get_user_model()

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=ProfileModel
        fields=('id','name','age','surname','create_at','updated_at')



class UserSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer()
    class Meta:
        model = UserModel
        fields = ('id', 'email','password','is_active', 'is_staff', 'is_superuser', 'last_login', 'create_at', 'updated_at','profile')
        # extra_kwargs = {"password": {'write_only': True}}
    def create(self, validated_data):
        profile=validated_data.pop('profile')
        user=UserModel.objects.create(**validated_data)
        ProfileModel.objects.create(**profile,user=user)
        return user


