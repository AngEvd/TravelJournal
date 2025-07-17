from trips.api_views import FeaturedTripsAPIView, PublicTripsAPIView
from django.urls import path

urlpatterns = [
    path('trips/featured-trips/', FeaturedTripsAPIView.as_view(), name='featured-trips'),
    path('trips/public-trips/', PublicTripsAPIView.as_view(), name='public-trips'),

]
