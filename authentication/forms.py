from django import forms
from django.contrib.auth.forms import SetPasswordForm, UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ChangePasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Exclude old_password field from rendering
        self.fields.pop("old_password", None)

    new_password1 = forms.CharField(
        label="New Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
