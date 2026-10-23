from time import timezone

from . import models
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = '__all__'

    def validate_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Release date cannot be in the future.")
        return value