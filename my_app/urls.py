from django.urls import path
# from .views import home
from .views import *

urlpatterns = [
    path('', home),
]