from django.contrib.auth.forms import UserCreationForm

from authentification.models import CustomUser


class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "first_name", "last_name", "password1", "password2", "age", "phone_number")
