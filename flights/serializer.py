from .models import Flight, Booking
from rest_framework import serializers
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'destination', 'time','price']

class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Booking
        fields = ['id','flight','date']
