from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    location = CountryField(blank=False, null=False)
    phone_number = PhoneNumberField(blank=False, null=False)

    def __str__(self):
        return self.username
