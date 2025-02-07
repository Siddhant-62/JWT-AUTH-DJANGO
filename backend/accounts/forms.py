from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import CustomUser

class CustomeUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        models= CustomUser
        fields=("email",)

class customUserChangeFrom(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

