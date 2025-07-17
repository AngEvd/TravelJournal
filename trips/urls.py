from django.urls import path
from .views import TripCreateView, TripDetailView, MyTripListView, TripEditView, TripDeleteView, PublicTripListView, toggle_like
from .api_views import PublicTripsAPIView

urlpatterns = [
    path('create/', TripCreateView.as_view(), name='trip_create'),
    path('<int:pk>/', TripDetailView.as_view(), name='trip_detail'),

    path('my_trips/', MyTripListView.as_view(), name='my_trip_list'),
    path('update/<int:pk>/', TripEditView.as_view(), name='trip_edit'),
    path('delete/<int:pk>/', TripDeleteView.as_view(), name='trip_delete'),

    path('dashboard/', PublicTripListView.as_view(), name='public_trip_list'),
    #path('dashboard/', PublicTripsAPIView.as_view(), name='public_trip_list'),

    path('<int:trip_id>/like/', toggle_like, name='toggle_like'),
]