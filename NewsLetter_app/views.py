import re
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import NewsLetter
# Create your views here.

def NewsLetterView(request):

    if request.method == "POST":

        if 'newsletter_mail' in request.POST:
            newsletter_email = request.POST['newsletter_mail']

            subscribers = NewsLetter.objects.all()
            subscribers_list = []
            for subscriber in subscribers:
                subscribers_list.append(subscriber.mail)
            if newsletter_email not in subscribers_list:
                data = NewsLetter()
                data.mail = newsletter_email
                data.save()
                messages.success(request, f"Thanks for ur interest {newsletter_email.upper()}")
                return redirect('home')
            else:
                messages.warning(request, "Sorry already subscribed!")
        else:
            messages.warning(request, "Invalid Form")
            print("Invalid Form")

    return HttpResponseRedirect("/")