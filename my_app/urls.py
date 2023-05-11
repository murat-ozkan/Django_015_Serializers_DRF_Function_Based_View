from django.urls import path
# from .views import app_home
from .views import *

urlpatterns = [
    path('', home),
]