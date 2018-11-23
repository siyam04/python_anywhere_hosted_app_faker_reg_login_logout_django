from django.shortcuts import render
# Same App importing
from second_app_user.models import User


def index2(request):
    """ Basic Views """
    templates = 'second_app_user/index.html'
    return render(request, templates)


def users(request):
    """All User's info"""
    user_list = User.objects.all()
    template_name = 'second_app_user/users.html'
    context = {'user_list': user_list}
    return render(request, template_name, context)
