from django.urls import path
from .views import (
    ContactView,
)

urlpatterns = [
    path('contactus/', ContactView, name='contactus'),
]
