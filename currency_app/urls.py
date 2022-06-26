from django.contrib import admin
from django.urls import path
from .views import (
    home,
    about,
    exchange,
    services,
    news,
    contact,
)
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('exchange/', exchange, name='exchange'),
    path('services/', services, name='services'),
    path('news/', news, name='news'),
    path('contact/', contact, name='contact'),
]
