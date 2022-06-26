from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def exchange(request):
    return render(request, "exchange.html")

def services(request):
    return render(request, "services.html")

def news(request):
    return render(request, "news.html")

def contact(request):
    return render(request, "contact.html")
