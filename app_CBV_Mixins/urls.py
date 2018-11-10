from django.urls import path
# Same App importing
from app_CBV_Mixins.views import (
    HomeView,
    SchoolListView,
    SchoolDetailView,
    SchoolCreateView,
    SchoolUpdateView,
    SchoolDeleteView,
)

# app_name = 'app_CBV_Mixins'

urlpatterns = [

    path('home', HomeView.as_view(), name='home'),
    path('list', SchoolListView.as_view(), name='list'),
    path('detail/<int:pk>', SchoolDetailView.as_view(), name='detail'),
    path('create', SchoolCreateView.as_view(), name='create'),
    path('update/<int:pk>', SchoolUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', SchoolDeleteView.as_view(), name='delete'),

]