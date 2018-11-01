from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, Textarea, SelectDateWidget, Select
# Same App importing
from fourth_app_reg_login_logout.models import UserProfileInfo


class UserForm(forms.ModelForm):
    """ Creating form for request user using built-in User class """
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        # This fields are built-in
        fields = ['username', 'email', 'password']
        # Customizing input fields
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            # 'password': TextInput(attrs={'class': 'form-control'}),
        }


class UserProfileInfoForm(forms.ModelForm):
    """ Creating form for UserProfileInfo class and use only two fields """
    class Meta:
        model = UserProfileInfo
        # We take username from built-in class in UserForm class.
        # So we need this two fields from UserProfileInfo class.
        fields = ['portfolio_site', 'profile_pic']
        widgets = {
            'portfolio_site': TextInput(attrs={'class': 'form-control'}),
        }

