import random
from django.db.models import Q
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
    
    def get_queryset(self):
        queryset = Trip.objects.filter(is_public=True)
        search_term = self.request.query_params.get('search', None)

        if search_term:
            queryset = queryset.filter(
                Q(title__icontains=search_term) |
                Q(destination__icontains=search_term) |
                Q(description__icontains=search_term)
            )

        return queryset.order_by('-created_at')
