from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return [
            # ---------- Core pages ----------
            'index',
            'channelmanager',
            'PMS',
            'BookingEngine',
            'price',
            'about',
            'cmapi',                              # channel-manager-api
            'mobileapp',                          # Mobile-app

            # ---------- Blog ----------
            'blog',
            'blogcmguide',                        # blog/channel-manager-guide
            'blogdyprice',                        # blog/dynamic-pricing-strategy
            'bloggoogleranking',                  # blog/hotel-google-ranking
            'channel_manager_price_india',        # blog/channel-manager-price-india
            'best_channel_manager_small_hotels',  # blog/best-channel-manager-small-hotels
            'channel_manager_vs_pms',             # blog/channel-manager-vs-pms

            # ---------- City pages ----------
            'hotel_software_ujjain',
            'hotel_software_indore',
            'hotel_software_jaipur',
            'hotel_software_goa',
            'hotel_software_varanasi',
            'hotel_software_udaipur',
            'hotel_software_ayodhya',
            'hotel_software_khatu_shyam',
            'hotel_software_somnath',
            'hotel_software_kolkata',
            'hotel_software_vijayawada',
            'hotel_software_nandyal',
            'hotel_software_tirupati',
            'hotel_software_shirdi',
            'hotel_software_amritsar',
            'hotel_software_haridwar',
            'hotel_software_rishikesh',
            'hotel_software_mathura_vrindavan',
            'hotel_software_prayagraj',
            'hotel_software_puri',
            'hotel_software_katra_vaishno_devi',
            'hotel_software_nashik',
        ]

    def location(self, item):
        return reverse(item)