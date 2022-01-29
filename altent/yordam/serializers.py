from rest_framework import serializers
from .models import Yordam

class YordamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yordam
        fields = ['id','text_uz', 'text_ru', 'text_eng']
        read_only_fields=("id",)


class UzSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text_uz=serializers.CharField(read_only=True)

class RuSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text_ru=serializers.CharField(read_only=True)

class EngSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text_eng=serializers.CharField(read_only=True)
    
        