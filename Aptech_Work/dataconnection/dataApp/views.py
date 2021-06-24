from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "About.html")


def contact(request):
    return render(request, "Contact.html")
