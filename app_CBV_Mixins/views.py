from django.urls import reverse_lazy
from django.http import HttpResponse
# Same app importing
from app_CBV_Mixins.models import School, Student
# Generic View
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)


class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')


class HomeView(TemplateView):
    """Home"""
    template_name = 'app_CBV_Mixins/home.html'

    def get_context_data(self, **kwargs):
        """Passing Values to Template"""
        # Making an object of 'HomeView class'
        # 'context' variable is an object of Parent class 'HomeView'.
        # 'super()' identifies that, 'get_context_data' is a parent class's function.
        # Here, we are using Recursion
        context = super().get_context_data(**kwargs)
        # '['injection']' is a key and 'Basic Injection!' is the value which will be shown on Template.
        context['injection'] = "Basic Injection!"
        return context


class SchoolListView(ListView):
    """
    If you don't pass in this attribute,
    Django will auto create a context name
    for you with object_list!
    Default would be 'school_list'
    Example of making your own:
    context_object_name = 'schools'
    """
    model = School
    # context_object_name = 'school_list' is a dictionary key which will pass to the template loop.
    # As like (for i in 'school_list')
    context_object_name = 'school_list'
    template_name = 'app_CBV_Mixins/school_list.html'


class SchoolDetailView(DetailView):
    """School Details"""
    model = School
    context_object_name = 'school_details'
    template_name = 'app_CBV_Mixins/school_detail.html'


class SchoolCreateView(CreateView):
    """Creating School"""
    fields = ('name', 'principal', 'location')
    model = School


class SchoolUpdateView(UpdateView):
    """Updating School"""
    fields = ('name', 'principal')
    model = School


class SchoolDeleteView(DeleteView):
    """Deleting School"""
    model = School
    success_url = reverse_lazy('list')
