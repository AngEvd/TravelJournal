from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django_countries.data import COUNTRIES
from django_countries.widgets import CountrySelectWidget
from phonenumber_field.formfields import PhoneNumberField
from phonenumbers import parse, is_valid_number, NumberParseException

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    location = forms.ChoiceField(
        choices=[('', 'Select country')] + sorted(COUNTRIES.items(), key=lambda x: x[1]),
        widget=CountrySelectWidget(attrs={'class': 'form-control'}),
        required=True,
    )

    phone_number = PhoneNumberField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'location',
                  'phone_number', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        country = self.cleaned_data.get('location')
        if not phone or not country:
            raise forms.ValidationError(
                "Please enter phone number and location.")

        try:
            parsed_phone = parse(str(phone), country)
            if not is_valid_number(parsed_phone):
                raise forms.ValidationError(
                    "Invalid phone number for the selected country.")
        except NumberParseException:
            raise forms.ValidationError("Invalid phone number format.")

        # Return phone as string in international format (E.164)
        return parsed_phone

    def save(self, commit=True):
        user = super().save(commit=False)
        # clean_phone_number returns phonenumbers.PhoneNumber object, convert to string
        phone = self.cleaned_data.get('phone_number')
        if hasattr(phone, 'as_e164'):
            user.phone_number = phone.as_e164
        else:
            # fallback if needed
            user.phone_number = str(phone)
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username does not exist.")

        return cleaned_data