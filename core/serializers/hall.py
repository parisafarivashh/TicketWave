from rest_framework import serializers
from ..models import Hall


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = ['title', 'created_at', 'updated_at']
        extra_kwargs = {
            'created_at': {'required': False},
            'updated_at': {'required': False},
        }

