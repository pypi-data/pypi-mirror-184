from rest_framework import serializers

from b2_utils.fields import PrimaryKeyRelatedFieldWithSerializer
from b2_utils.models import Address, City, Phone


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ["id", "country_code", "area_code", "number", "created", "modified"]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            "id",
            "name",
            "state",
            "created",
            "modified",
        ]


class AddressSerializer(serializers.ModelSerializer):
    city = PrimaryKeyRelatedFieldWithSerializer(
        CitySerializer, queryset=City.objects.all()
    )

    class Meta:
        model = Address
        fields = [
            "id",
            "city",
            "street",
            "number",
            "additional_info",
            "district",
            "zip_code",
            "created",
            "modified",
        ]


class PrimaryKeyRelatedFieldWithSerializer(serializers.PrimaryKeyRelatedField):
    def __init__(self, representation_serializer, **kwargs):
        self.representation_serializer = representation_serializer
        super().__init__(**kwargs)

    def to_representation(self, value):
        if callable(value):
            return self.representation_serializer(value.all(), many=True).data

        instance = self.queryset.get(pk=value.pk)

        return self.representation_serializer(instance).data
