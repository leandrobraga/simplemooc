from django.shortcuts import render


def home(request):

    return render(request, 'home.html', {"usuario": "leandro"})


def contact(request):

    return render(request, 'contact.html')
