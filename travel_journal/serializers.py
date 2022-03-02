from rest_framework import serializers

from .models import TravelJournal


class TravelJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelJournal
        fields = '__all__'
        read_only_fields = ['id']


class TravelJournalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelJournal
        fields = ["title", "description", "photo", "city", "place_name", "lat", "long"]
