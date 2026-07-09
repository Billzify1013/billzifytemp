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
            'mobileapp',
            'blogdyprice',                        # blog/dynamic-pricing-strategy
            'bloggoogleranking',                  # blog/hotel-google-ranking
            'channel_manager_price_india',        # blog/channel-manager-price-india
            'best_channel_manager_small_hotels',  # blog/best-channel-manager-small-hotels
            'channel_manager_vs_pms',             # blog/channel-manager-vs-pms
        ]

    def location(self, item):
        return reverse(item)