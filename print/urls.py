
from django.urls import path,include
from .views import *

urlpatterns = [
    path('main/<int:order>', mainprint),
    path('checkavailablity',checkavailability),
]
