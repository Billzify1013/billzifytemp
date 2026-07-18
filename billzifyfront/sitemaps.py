from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
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
            'cmapi',                                    # channel-manager-api
            'mobileapp',                                # Mobile-app

            # ---------- Pillar guides ----------
            'hotel_channel_manager',                    # /hotel-channel-manager/
            'hotel_pms_software',                       # /hotel-pms-software/
            'hotel_booking_engine',                     # /hotel-booking-engine/
            'hotel_billing_software',                   # /hotel-billing-software/
            'list_hotel_on_makemytrip',                 # /list-hotel-on-makemytrip/
            'list_hotel_on_booking_com',                # /list-hotel-on-booking-com/
            'list_hotel_on_airbnb',                     # /list-hotel-on-airbnb/

            # ---------- OTA-specific pages ----------
            'makemytrip_channel_manager',
            'booking_com_channel_manager',
            'goibibo_channel_manager',
            'agoda_channel_manager',
            'airbnb_channel_manager',

            # ---------- Property type pages ----------
            'homestay_management_software',
            'resort_management_software',
            'guest_house_management_software',
            'boutique_hotel_software',
            'service_apartment_management_software',

            # ---------- Blog ----------
            'blog',
            'blogcmguide',                              # blog/channel-manager-guide
            'blogdyprice',                              # blog/dynamic-pricing-strategy
            'bloggoogleranking',                        # blog/hotel-google-ranking
            'channel_manager_price_india',              # blog/channel-manager-price-india
            'best_channel_manager_small_hotels',        # blog/best-channel-manager-small-hotels
            'channel_manager_vs_pms',                   # blog/channel-manager-vs-pms

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

    def priority(self, item):
        # Highest — homepage and main money pages
        if item in ('index', 'channelmanager', 'hotel_channel_manager'):
            return 1.0
        # High — core product pages and pillar guides
        if item in ('PMS', 'BookingEngine', 'price',
                    'hotel_pms_software', 'hotel_booking_engine',
                    'hotel_billing_software'):
            return 0.9
        # Everything else
        return 0.8