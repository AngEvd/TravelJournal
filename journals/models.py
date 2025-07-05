from django.db import models


class JournalEntry(models.Model):
    trip = models.ForeignKey("trips.Trip", on_delete=models.CASCADE, related_name="journal_entries")
    title = models.CharField(max_length=100)
    content = models.TextField()
    entry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-entry_date"]
        verbose_name = "Journal Entry"
        verbose_name_plural = "Journal Entries"

    def __str__(self):
        return f"{self.title} - {self.entry_date}"


class Photo(models.Model):
    journal_entry = models.ForeignKey("journals.JournalEntry", on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="journal_photos/")
    caption = models.CharField(max_length=200, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for {self.journal_entry.title} - {self.journal_entry.entry_date}"
