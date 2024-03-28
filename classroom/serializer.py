#serializers.py
from dataclasses import dataclass
from datetime import datetime
from rest_framework import serializers
from .models import ClassromEntity

class WeatherSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, allow_blank=True)
    date = serializers.DateTimeField() 
    description = serializers.CharField(max_length=255, allow_blank=True)
    discipline = serializers.CharField(max_length=255, allow_blank=True)
    reservation = serializers.BooleanField()

    def create(self, validated_data):
        return ClassromEntity(**validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)