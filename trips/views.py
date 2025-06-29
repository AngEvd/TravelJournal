from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

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


class TripDetailView(LoginRequiredMixin, DetailView):
    model = Trip
    template_name = 'trips/trip_detail.html'
    context_object_name = 'trip'
