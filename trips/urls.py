from django.urls import path
from .views import TripCreateView, TripDetailView, MyTripListView, TripEditView

urlpatterns = [
    path('create/', TripCreateView.as_view(), name='trip_create'),
    path('<int:pk>/', TripDetailView.as_view(), name='trip_detail'),

    path('my_trips/', MyTripListView.as_view(), name='my_trip_list'),
    path('update/<int:pk>/', TripEditView.as_view(), name='trip_edit'),
]