from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from NewsLetter_app.models import NewsLetter
# Create your views here.
def SearchView(request):
    if request.method=="POST":
        query = request.POST['query']
        print("query : ",query)
        newsletter_mails = NewsLetter.objects.all().filter(Q(mail__icontains=query))
        context = {
            "mails":newsletter_mails,
            "query":query,
        }
        return render(request, 'search.html', context=context)
    return HttpResponseRedirect('/')