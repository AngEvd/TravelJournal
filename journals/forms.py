from .models import JournalEntry, Photo
from django import forms
from django.forms import inlineformset_factory, BaseInlineFormSet


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

    def __init__(self, *args, **kwargs):
        self.trip = kwargs.pop("trip", None)  # grab the trip
        super().__init__(*args, **kwargs)

    def clean_entry_date(self):
        entry_date = self.cleaned_data.get("entry_date")

        if self.trip:
            if entry_date < self.trip.start_date or entry_date > self.trip.end_date:
                raise forms.ValidationError(
                    f"Entry date must be between {self.trip.start_date} and {self.trip.end_date}."
                )
        return entry_date

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["image", "caption"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False

# class RequiredImageBaseFormSet(BaseInlineFormSet):
#     def clean(self):
#         super().clean()
#         for form in self.forms:
#             if not hasattr(form, "cleaned_data"):
#                 continue  # Skip forms with uncleaned data
#
#             if self.can_delete and form.cleaned_data.get("DELETE", False):
#                 continue  # Skip forms marked for deletion
#
#             is_new = not form.instance.pk
#             image = form.cleaned_data.get("image")
#
#             # If it's a new form with any data, require image
#             if is_new and form.has_changed():
#                 if not image:
#                     form.add_error("image", "This field is required.")



PhotoFormSet = inlineformset_factory(
    parent_model=JournalEntry,
    model=Photo,
    form=PhotoForm,
    fields=["image", "caption"],
    extra=1,
    max_num=10,
    can_delete=True,
)