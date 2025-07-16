import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Trip
from .serializers import TripSerializer


class FeaturedTripsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        trips = list(Trip.objects.filter(is_public=True))
        random.shuffle(trips)
        serializer = TripSerializer(trips[:4], many=True)
        return Response(serializer.data)


class PublicTripsAPIView(generics.ListAPIView):
    serializer_class = TripSerializer
    queryset = Trip.objects.filter(is_public=True)