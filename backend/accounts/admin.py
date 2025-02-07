from django.contrib import admin
from .models import CustomUser
from .forms import customUserChangeFrom,CustomeUserCreationForm
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomAdminUser(UserAdmin):
    add_form =CustomeUserCreationForm
    form = customUserChangeFrom

    model= CustomUser



# Register your models here.
