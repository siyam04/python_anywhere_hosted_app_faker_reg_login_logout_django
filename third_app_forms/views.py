from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
# Same App importing
from third_app_forms.models import User
from third_app_forms.forms import NewUserForm


def welcome(request):
    """ Welcoming view """
    template_name = 'third_app_forms/welcome.html'
    return render(request, template_name)


def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return welcome(request)
        else:
            print('ERROR!')

    else:
        form = NewUserForm()

    return render(request, template_name='third_app_forms/form_page.html', context={'form': form})



# ----------------------------------------------------------------------------------------------------------------------
# def form_name_view(request):
#     """ Basic Form for take input from Users"""
#     form = FormName()
#     if request.method == 'POST':
#         form = FormName(request.POST)
#         if form.is_valid():
#             print("Form Validation Success. Prints in console.")
#             print("Name" + form.cleaned_data['name'])
#             print("Email" + form.cleaned_data['email'])
#             print("Verify Email" + form.cleaned_data['verify_email'])
#             print('Text' + form.cleaned_data['text'])
#             # name = form.cleaned_data['name']
#             # email = form.cleaned_data['email']
#             # text = form.cleaned_data['text']
#             # instance = authenticate(name=name, email=email, text=text)
#             # form.save(instance)
#             # return redirect('form-create-success')
#     # else:
#     #     # If there is no POST request, shows empty form
#     #     form = FormName()
#
#     return render(request, template_name='third_app_forms/form_page.html', context={'form': form})




