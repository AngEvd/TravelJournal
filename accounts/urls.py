from django.contrib.auth.views import LogoutView
from django.urls import path
from django.urls.conf import include

from accounts import views

urlpatterns = [
    path('', include([
        path('register/', views.RegisterUserView.as_view(), name='register'),
        path('login/', views.LoginUserView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(next_page="index"), name='logout'),
    ])),
]
