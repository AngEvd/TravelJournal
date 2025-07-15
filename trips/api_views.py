from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Trip
from .serializers import TripSerializer
import random


class FeaturedTripsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        trips = list(Trip.objects.filter(is_public=True))
        random.shuffle(trips)
        serializer = TripSerializer(trips[:4], many=True)
        return Response(serializer.data)
