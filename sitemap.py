from django.contrib.sitemaps import Sitemap
from django.urls import reverse



class StaticSitemap(Sitemap):
    """
    Карта-сайта для статичных страниц
    """

    def items(self):
        return ['index','Gallery','Aboutus']
    
    def location(self, item):
        return reverse(item)