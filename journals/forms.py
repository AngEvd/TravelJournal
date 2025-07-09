from .models import JournalEntry, Photo
from django import forms
from django.forms import modelformset_factory


class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ["title", "content", "entry_date"]
        widgets = {
            "entry_date": forms.DateInput(attrs={"type": "date"}),
        }
        labels = {
            "title": "Title",
            "content": "Content",
            "entry_date": "Entry Date",
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["image", "caption"]


PhotoFormSet = modelformset_factory(
        Photo,
        form=PhotoForm,
        extra=1,
        max_num=10,
        can_delete=True,
    )