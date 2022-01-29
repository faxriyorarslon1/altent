from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
        read_only_fields=("id",)


class UzSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname = serializers.CharField(read_only=True)
    role_uz=serializers.CharField(read_only=True)
    text_uz=serializers.CharField(read_only=True)
    motto_uz=serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)

class RuSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname_ru = serializers.CharField(read_only=True)
    role_ru=serializers.CharField(read_only=True)
    text_ru=serializers.CharField(read_only=True)
    motto_ru=serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)

class EngSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname = serializers.CharField(read_only=True)
    role_eng=serializers.CharField(read_only=True)
    text_eng=serializers.CharField(read_only=True)
    motto_eng=serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)


    
        