from django import forms

from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import MyUser


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    email = forms.CharField(label='Your Email address', widget=forms.TextInput)
    name = forms.CharField(label='Your Name', widget=forms.TextInput)
    phone_no = forms.CharField(label='Your Phone Number', widget=forms.NumberInput)
    password1 = forms.CharField(label='Your Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Your Password', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'name', 'phone_no')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'name', 'phone_no', 'is_active', 'is_admin')



class UserLoginForm(forms.ModelForm):
    """A form for Lohin users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    class Meta:
        model = MyUser
        fields = ('email', 'password')

