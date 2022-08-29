from rest_framework import serializers
from .models import Dog

class DogSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ("id", "owner", "name", "description", "created_at")
    model = Dog