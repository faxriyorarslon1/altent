from rest_framework import serializers
from .models import Pupil

class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupil
        fields = "__all__"
        read_only_fields=("id",)


class UzSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname = serializers.CharField(read_only=True)
    text_uz=serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)

class RuSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname_ru = serializers.CharField(read_only=True)
    text_ru=serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)

class EngSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname = serializers.CharField(read_only=True)
    text_eng=serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)


