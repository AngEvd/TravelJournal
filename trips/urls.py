from django.urls import path
from .views import TripCreateView, TripDetailView

urlpatterns = [
    path('create/', TripCreateView.as_view(), name='trip_create'),
    path('<int:pk>/', TripDetailView.as_view(), name='trip_detail'),
]