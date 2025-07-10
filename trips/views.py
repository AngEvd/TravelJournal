from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .forms import TripForm
from .models import Trip, Like


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
        user = self.request.user
        context['journal_entries'] = trip.journal_entries.all()
        context['has_liked'] = (user.is_authenticated and Like.objects.filter(user=user, trip=trip).exists())
        context['like_count'] = trip.likes.count()
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
    

class PublicTripListlView(ListView):
    model = Trip
    template_name = 'trips/public_trip_list.html'
    context_object_name = 'public_trips'

    def get_queryset(self):
        return Trip.objects.filter(is_public=True).order_by('-created_at')
  

@login_required
def toggle_like(request, trip_id):
    if request.method == 'POST':
        trip = get_object_or_404(Trip, pk=trip_id)
        like, created = Like.objects.get_or_create(user=request.user, trip=trip)

        if not created:
            like.delete()
            has_liked = False
        else:
            has_liked = True

        return JsonResponse({
            'success': True,
            'has_liked': has_liked,
            'like_count': trip.likes.count(),
        })

    return JsonResponse({'success': False}, status=400)
