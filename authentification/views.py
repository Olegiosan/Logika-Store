from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from authentification.forms import CreateUserForm
from authentification.models import CustomUser


# Create your views here.
class LoginUserView(LoginView):
    template_name = "authentification/user_login.html"
    authentication_form = AuthenticationForm

class CreateUser(CreateView):
    template_name = "authentification/create_user.html"
    form_class = CreateUserForm
    success_url = reverse_lazy("user_login")
    model = CustomUser