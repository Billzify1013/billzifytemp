from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return [
            'index',
            'channelmanager',
            'PMS',
            'BookingEngine',
            'price',
            'about',
            'blog',
            'cmapi',        # channel-manager-api page
            'blogcmguide',  # blog/channel-manager-guide page
            'bloggoogleranking',
        ]

    def location(self, item):
        return reverse(item)