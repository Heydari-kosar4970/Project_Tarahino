from django.shortcuts import render


def index_page(request):
    return render(request, 'public/index.html')


def contactus_page(request):
    return render(request, 'public/Contactus.html')


def aboutus_page(request):
    return render(request, 'public/aboutus.html')

