from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return [
            'index',           # index page
            'channelmanager', # channel manager page
            'PMS',            # PMS page
            'BookingEngine', # booking engine page
            'price',          # pricing page
            'about',          # about page
        ]

    def location(self, item):
        return reverse(item)