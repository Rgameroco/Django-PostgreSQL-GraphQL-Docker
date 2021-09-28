from rest_framework import serializers
from fieldWorker.models import FUNCTION_CHOICES,FieldWorker
from django.utils import timezone

class FieldWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldWorker
        fields = ["id","first_name","last_name","function","created_at"]
    def create(self, validated_data):
        return FieldWorker.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.function = validated_data.get('function', instance.function)
        instance.save()
        return instance