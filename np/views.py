from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .forms import SellsForm
from .models import Sells

def index(request):
    if request.method == 'POST':
        fm = SellsForm(request.POST)
        if fm.is_valid():
            fm.save()
        else:
            return HttpResponse('<h1>Enter vailid data</h1>')

    fm = SellsForm()
    md = Sells.objects.all()


    return render(request, 'index.html',{'form' : fm,'model' : md})
    #return render(request, 'index.html')