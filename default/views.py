from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def IndexView(request):
    return render(request, "index.html", {'title': 'Технологии механической обработки'})

def GalleryView(request):
    return render(request, "gallery.html", {'title': 'Галерея'})
def AboutusView(request):
    return render(request, "aboutus.html", {'title': 'О компании ООО "ТехМех"'})
