from rest_framework import serializers
from .models import Adocao


class AdocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adocao
        fields = ("id", "email", "value", "pet")
