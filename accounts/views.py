from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView

from accounts.forms import UserRegistrationForm

User = get_user_model()


class RegisterUserView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


class LoginUserView(LoginView):
    model = User
    template_name = 'accounts/login.html'

