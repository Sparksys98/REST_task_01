
from .models import Flight, Booking
from datetime import datetime
from rest_framework.generics import ListAPIView
from .serializer import ListSerializer, BookingListSerializer
class ListView(ListAPIView):
    queryset=Flight.objects.all()
    serializer_class = ListSerializer

class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class=BookingListSerializer
