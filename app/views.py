from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *

def djangoforms(request):
    STO=StudentForm()
    d={'STO':STO}
    if request.method=='POST':
        STO=StudentForm(request.POST)
        if STO.is_valid():
            return HttpResponse(str(STO.cleaned_data))
        else:
            return HttpResponse('invalid data')
    return render(request,'djangoforms.html',d)