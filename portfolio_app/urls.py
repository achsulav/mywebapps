from django.urls import path
from .views import home, error  # Import your views

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('error/', error, name='error'),  # Error page  
]