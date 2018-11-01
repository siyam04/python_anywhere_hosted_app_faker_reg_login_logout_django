from django import forms
from django.forms import (
    TextInput,
    Textarea,
    SelectDateWidget,
    Select,
)
# Same App importing
from third_app_forms.models import User


class NewUserForm(forms.ModelForm):
    """ Creating Model Form """
    # Custom Field adding to the form
    # username = forms.CharField(max_length=10)
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['username', 'first_name', 'last_name', 'email', 'verify_email']
        # exclude = ['last_name']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'verify_email': TextInput(attrs={'class': 'form-control'}),
        }





# ----------------------------------------------------------------------------------------------------------------------
        # widgets = {
        #     'title': TextInput(attrs={'class': 'form-control'}),
        #     'category': Select(attrs={'class': 'form-control'}),
        #     'published': SelectDateWidget(attrs={'class': 'form-control'}),
        #     'content': Textarea(attrs={'class': 'form-control'}),
        # }

        # widgets = {
        #     'content_type': forms.HiddenInput(attrs={'class': 'form-control'}),
        #     'object_id': forms.HiddenInput(attrs={'class': 'form-control'}),
        #     'parent': forms.HiddenInput(attrs={'class': 'form-control'}),
        #     'leave_a_message': forms.TextInput(attrs={'class': 'form-control'}),
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        # }

# ----------------------------------------------------------------------------------------------------------------------
# from django import forms
# from django.core import validators
# # for clean_bot_catcher method
# from django.core.exceptions import ValidationError


# If we want to add custom validator to any field
# def check_for_a(self, value):
#     if value[0].lower() != 'a':
#         raise forms.ValidationError("Name Needs To Start with a")


# class FormName(forms.Form):
#     """ Very Basic Example of a Django Form """
#     name = forms.CharField(max_length=50)
#     email = forms.EmailField(widget=forms.EmailInput)
#     verify_email = forms.EmailField(label='Enter your email again:')
#     text = forms.CharField(widget=forms.Textarea)
#
#     # Extra security for bots. They only see the HTML.
#     bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput,
#                                   validators=[validators.MaxLengthValidator(0)])


    # For detect Bots, who may able to crash the site. We use Django validators for this method. No need to create this.
    # def clean_bot_catcher(self):
    #     bot_catcher = self.cleaned_data['bot_catcher']
    #     if len(bot_catcher) > 0:
    #         raise ValidationError('Gotcha BOT!')
    #     return bot_catcher
# ----------------------------------------------------------------------------------------------------------------------


