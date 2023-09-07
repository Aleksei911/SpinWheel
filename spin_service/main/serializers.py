from rest_framework import serializers
from .models import RoundCurrentValues, Log


class RoundCurrentValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoundCurrentValues
        fields = '__all__'


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'
