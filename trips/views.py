from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from .forms import TripForm
from .models import Trip


class TripCreateView(LoginRequiredMixin, CreateView):
    model = Trip
    form_class = TripForm
    template_name = 'trips/trip_entry.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('trip_detail', kwargs={'pk': self.object.pk})


class TripDetailView(DetailView):
    model = Trip
    template_name = 'trips/trip_detail.html'
    context_object_name = 'trip'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = self.get_object()
        context['journal_entries'] = trip.journal_entries.all()
        return context


class MyTripListView(LoginRequiredMixin, ListView):
    model = Trip
    template_name = 'trips/my_trip_list.html'
    context_object_name = 'trips'

    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user)


class TripEditView(LoginRequiredMixin, UpdateView):
    model = Trip
    form_class = TripForm
    template_name = 'trips/trip_entry.html'

    def get_success_url(self):
        return reverse_lazy('trip_detail', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user)
    

class PublicTripDetailView(ListView):
    model = Trip
    template_name = 'trips/public_trip_list.html'
    context_object_name = 'public_trips'

    def get_queryset(self):
        return Trip.objects.filter(is_public=True).order_by('-created_at')
    
    def get_object(self, queryset=None):
        trip = super().get_object(queryset)
        if trip.is_public or self.request.user.is_authenticated:
            return trip

