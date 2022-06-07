from rest_framework import serializers
from .models import Adocao
from pet.serializers import PetSerializer
from pet.models import Pet


class AdocaoSerializer(serializers.ModelSerializer):
    pet = PetSerializer(many=False, read_only=True)
    pet_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=Pet.objects.all()
    )

    class Meta:
        model = Adocao
        fields = ("id", "email", "donation", "pet", "pet_id")

    def create(self, validated_data):
        validated_data["pet"] = validated_data.pop("pet_id")
        return super().create(validated_data)

    def validate_value(self, donation):
        if donation < 10:
            raise serializers.ValidationError(
                "Valor não deve ser inferior a 10"
            )
        if donation > 100:
            raise serializers.ValidationError(
                "Valor não deve ser superior a 100"
            )
        return donation
