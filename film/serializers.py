from .models import *
from rest_framework import serializers

class AktyorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ism = serializers.CharField(max_length=50)
    tugilgan_yil = serializers.DateField()
    davlat = serializers.CharField(max_length=30, allow_blank=True)
    jins = serializers.CharField(max_length=30)

    def validate_ism(self, qiymat):
        if len(qiymat) < 3:
            raise serializers.ValidationError("Ism bunaqa kalta bo'lishi mumkin emas!")
        return qiymat

    def validate_jins(self, qiymat):
        if qiymat != "Erkak" and qiymat != "Ayol":
            raise serializers.ValidationError("Bunday jins bo'lishi mumkin emas!")
        return qiymat

class TarifSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=50)
    muddat = serializers.CharField(max_length=50)
    narx = serializers.IntegerField()

class KinoSerializer(serializers.ModelSerializer):
    aktyorlar = AktyorSerializer(many=True)
    class Meta:
        model = Kino
        fields = '__all__'

class KinoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kino
        fields = '__all__'

class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = '__all__'