from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def SearchView(request):
    if request.method=="POST":
        query = request.POST['query']
        print("query : ",query)
    return HttpResponseRedirect('/')