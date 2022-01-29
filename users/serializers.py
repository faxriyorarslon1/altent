from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()

        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'last_name','password')

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def to_representation(self, ins):
       
        return {
            "id": ins.id,
            "email": ins.email,
            "username": ins.username,
            "last_name": ins.last_name,
        }




class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'id': self.user.id})
        data.update({'username': self.user.username})
        data.update({'last_name': self.user.last_name})
        data.update({'email': self.user.email})
       

        return data


