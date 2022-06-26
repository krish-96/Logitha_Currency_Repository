from django.urls import path
from .views import (
    NewsLetterView,
)

urlpatterns = [
    path('newsletter/', NewsLetterView, name='newsletter'),
]
