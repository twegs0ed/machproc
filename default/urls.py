from django.urls import path
from .views import IndexView, GalleryView, AboutusView
 
urlpatterns = [
    path('', IndexView, name='index'),
    path('gallery', GalleryView, name='Gallery'),
    path('about-us', AboutusView, name='Aboutus')
]