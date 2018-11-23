from django.urls import path
# Same App importing
from .views import users, index2

# Custom App URLs
urlpatterns = [
    path('users', users, name='users'),
    path('index2', index2, name='index2'),
]