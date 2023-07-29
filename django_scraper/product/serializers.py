from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, URLField

class DataSerializer(serializers.ModelSerializer):
    name = CharField(required=True)
    price = CharField(required=True)
    url = URLField(required=True)
    image_url = URLField(required=True)

    class Meta:
        model = models.data
        fields = (
            'name',
            'price',
            'url',
            'image_url'
        )