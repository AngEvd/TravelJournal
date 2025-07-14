from django.urls import path
from .views import JournalEntryCreateView, JournalEntryDetailView, JournalEntryUpdateView, JournalEntryDeleteView

urlpatterns = [
    path("trip/<int:trip_id>/journals/new/", JournalEntryCreateView.as_view(), name="journal_entry_create"),
    path("<int:pk>/", JournalEntryDetailView.as_view(),name="journal_entry_detail"),
    path("<int:pk>/edit/", JournalEntryUpdateView.as_view(), name="journal_entry_update"),
    path("<int:pk>/delete/", JournalEntryDeleteView.as_view(), name="journal_entry_delete"),
    ]
