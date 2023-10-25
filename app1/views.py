from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import python
from .models import Sql
from .models import Ml
def home1(request):
    template=loader.get_template("home1.html")
    return HttpResponse(template.render())
def examcat(request):
    template=loader.get_template("examcat.html")
    return HttpResponse(template.render())
def pythontest(request):
    python1 = python.objects.all().values()
    return render(request,'python.html',{'python':python1})

def home1r(request):
    return HttpResponseRedirect(reverse('home1'))
def sqltest(request):
    sql1=Sql.objects.all()
    return render(request,'sql.html',{'sql':sql1})
def mltest(request):
    ml1=Ml.objects.all()
    return render(request,'ml.html',{'ml':ml1})