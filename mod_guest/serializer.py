from rest_framework import serializers
from .models import huesped

class HuespedSerializer(serializers.ModelSerializer):
    class Meta:
        model = huesped
        fields = "__all__"

