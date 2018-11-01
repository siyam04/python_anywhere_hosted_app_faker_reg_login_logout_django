from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Same App importing
from fourth_app_reg_login_logout.models import UserProfileInfo
from fourth_app_reg_login_logout.forms import UserForm, UserProfileInfoForm


def welcome_user(request):
    """ Welcoming view """
    template_name = 'fourth_app_reg_login_logout/index.html'
    return render(request, template_name)


def register(request):
    """ User registration """
    # Ensuring that someone registered or not.
    # This keyword = registered, is used to the registration.html
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save UserForm directly to the database
            user = user_form.save()
            # Hashing the password using set_password method
            user.set_password(user.password)
            # Saving the Hashed password to the database
            user.save()

            # Linking between two forms (UserForm and UserProfileInfoForm)
            profile = profile_form.save(commit=False)
            # user = UserForm, profile = UserProfileInfoForm,
            # profile.user = the user which connected by OneToOneField to the User class in the UserProfileInfo model.
            profile.user = user

            # request.FILES = images, data, etc
            # if 'profile_pic' in request.FILES = If client's POST request has images, data
            if 'profile_pic' in request.FILES:
                # Then set the POST request to the model's profile_pic field.
                profile.profile_pic = request.FILES['profile_pic']

            # Save the total form to the database
            profile.save()

            # Ensuring that someone is registered now.
            # This keyword = registered, is used to the registration.html
            registered = True
            # Automatic login after registration
            # return user_login(request)
            # Shows login form after registration
            return redirect('user-login')

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'fourth_app_reg_login_logout/registration.html', {'user_form': user_form,
                                                                             'profile_form': profile_form,
                                                                             'registered': registered})


def user_login(request):
    """ User login """
    if request.method == 'POST':
        # This username and password supplied from login form's input name
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authentication using built-in method
        user = authenticate(username=username, password=password)

        # If User is available,
        if user:
            # If User is active, allow him to Login
            if user.is_active:
                login(request, user)
                # Return to homepage.
                return welcome_user(request)
            else:
                # Return to registration form.
                return redirect('register')

        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        # Nothing has been provided for username or password.
        return render(request, 'fourth_app_reg_login_logout/login.html', {})


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return welcome_user(request)



