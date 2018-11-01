from django.urls import path
# Same App importing
from .views import index

# Custom App URLs
urlpatterns = [
    path('index', index, name='index'),
]