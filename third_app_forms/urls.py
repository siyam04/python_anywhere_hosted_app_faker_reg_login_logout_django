from django.urls import path
# Same App importing
from third_app_forms.views import welcome, users

urlpatterns = [

    path('welcome', welcome, name='welcome'),
    path('form-page', users, name='form-page'),

]