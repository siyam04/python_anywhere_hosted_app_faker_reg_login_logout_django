from django.shortcuts import render
# Same App importing
from .models import Topic, WebPage, AccessRecord


def index(request):
    """All Website's Name and Date"""
    web_pages_list = AccessRecord.objects.all()
    template_name = 'first_app/index.html'
    context = {'web_pages_list': web_pages_list}
    return render(request, template_name, context)

