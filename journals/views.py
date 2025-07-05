from django.apps import apps
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, UpdateView
from .models import JournalEntry, Photo
from .forms import JournalEntryForm, PhotoFormSet


# Create your views here.
class JournalEntryCreateView(View):
    def get(self, request, trip_id):
        Trip = apps.get_model("trips", "Trip")
        trip = get_object_or_404(Trip, id=trip_id)
        entry_form = JournalEntryForm()
        photo_formset = PhotoFormSet(queryset=Photo.objects.none())
        return render(request, "journals/journal_entry_form.html", {
            "trip": trip,
            "entry_form": entry_form,
            "photo_formset": photo_formset,
        })

    def post(self, request, trip_id):
        Trip = apps.get_model("trips", "Trip")
        trip = get_object_or_404(Trip, id=trip_id)
        entry_form = JournalEntryForm(request.POST)
        photo_formset = PhotoFormSet(request.POST, request.FILES)

        if entry_form.is_valid() and photo_formset.is_valid():
            journal_entry = entry_form.save(commit=False)
            journal_entry.trip = trip
            journal_entry.save()

            for form in photo_formset:
                if form.cleaned_data:
                    photo = form.save(commit=False)
                    photo.journal_entry = journal_entry
                    photo.save()

            return redirect("journal_entry_detail", pk=journal_entry.pk)

        return render(request, "journals/journal_entry_form.html", {
            "trip": trip,
            "entry_form": entry_form,
            "photo_formset": photo_formset,
        })


class JournalEntryDetailView(DetailView):
    model = JournalEntry
    template_name = "journals/journal_entry_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["journal_entry"] = self.object  # Add custom context name
        return context


class JournalEntryUpdateView(UpdateView):
    model = JournalEntry
    form_class = JournalEntryForm
    template_name = "journals/journal_entry_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['journal_entry'] = self.object
        return context

    def get_success_url(self):
        return reverse_lazy('journal_entry_detail', kwargs={'pk': self.object.pk})