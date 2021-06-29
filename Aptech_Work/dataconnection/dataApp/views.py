from django.shortcuts import render, HttpResponse
from _datetime import datetime
from . import models

# Create your views here.
from .models import Contact


def index(request):
    obj = Contact.objects.all()

    context = {
        'object': obj
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "About.html")


def contact(request):
    flag = False
    if request.method == "POST":
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        phone1 = request.POST.get('phone')
        message1 = request.POST.get('message')
        date1 = datetime.now()
        modeldata = Contact(name=name1, email=email1, phone=phone1, message=message1, date=date1)
        modeldata.save()
        flag = True

    context = {
        'flag': flag
    }
    return render(request, "Contact.html", context)
