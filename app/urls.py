from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

from django.contrib.sitemaps.views import sitemap
from billzifyfront.sitemaps import StaticViewSitemap

from .views import RobotsTxtView

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.index,name="index"),
    path('price/', views.price,name="price"),
    path('about/', views.about,name="about"),
    path('channelmanager/', views.channelmanager,name="channelmanager"),
    path('PMS/', views.PMS,name="PMS"),
    path('BookingEngine/', views.BookingEngine,name="BookingEngine"),
    path('addfreedemo/', views.index,name="addfreedemo"),
    path('terms/', views.terms,name="terms"),
    path('privcy/', views.privcy,name="privcy"),
    path('refund/', views.refund,name="refund"),
    path('website/', views.website,name="website"),
    path('blog/', views.blog,name="blog"),
    path('channel-manager-api/', views.cmapi,name="cmapi"),
    path('blog/channel-manager-guide/', views.blogcmguide,name="blogcmguide"),
    path('blog/dynamic-pricing-strategy/', views.blogdyprice,name="blogdyprice"),
    path('blog/channel-manager-price-india/', views.channel_manager_price_india,name="channel_manager_price_india"),
    path('blog/best-channel-manager-small-hotels/', views.best_channel_manager_small_hotels,name="best_channel_manager_small_hotels"),
    path('blog/channel-manager-vs-pms/', views.channel_manager_vs_pms,name="channel_manager_vs_pms"),
    path('blog/hotel-google-ranking/', views.bloggoogleranking, name="bloggoogleranking"),
    path('Mobile-app/', views.mobileapp, name="mobileapp"),


    path('proxy-create-demo/', views.forward_to_live_api, name='proxy_create_demo'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, 
         name='django.contrib.sitemaps.views.sitemap'),

    path('robots.txt', RobotsTxtView.as_view(), name='robots'),
    path('delete-account/', views.delete_account_view, name='delete_account_view'),


    # blog pages more here
    path('hotel-software-ujjain/', views.hotel_software_ujjain, name="hotel_software_ujjain"),
    path('hotel-software-indore/', views.hotel_software_indore, name="hotel_software_indore"),
    path('hotel-software-jaipur/', views.hotel_software_jaipur, name="hotel_software_jaipur"),
    path('hotel-software-goa/', views.hotel_software_goa, name="hotel_software_goa"),
    path('hotel-software-varanasi/', views.hotel_software_varanasi, name="hotel_software_varanasi"),
    path('hotel-software-udaipur/', views.hotel_software_udaipur, name="hotel_software_udaipur"),
    path('hotel-software-ayodhya/', views.hotel_software_ayodhya, name="hotel_software_ayodhya"),
    path('hotel-software-khatu-shyam/', views.hotel_software_khatu_shyam, name="hotel_software_khatu_shyam"),
    path('hotel-software-somnath/', views.hotel_software_somnath, name="hotel_software_somnath"),
    path('hotel-software-kolkata/', views.hotel_software_kolkata, name="hotel_software_kolkata"),
    path('hotel-software-vijayawada/', views.hotel_software_vijayawada, name="hotel_software_vijayawada"),
    path('hotel-software-nandyal/', views.hotel_software_nandyal, name="hotel_software_nandyal"),

    path('hotel-software-tirupati/', views.hotel_software_tirupati, name="hotel_software_tirupati"),
    path('hotel-software-shirdi/', views.hotel_software_shirdi, name="hotel_software_shirdi"),
    path('hotel-software-amritsar/', views.hotel_software_amritsar, name="hotel_software_amritsar"),
    path('hotel-software-haridwar/', views.hotel_software_haridwar, name="hotel_software_haridwar"),
    path('hotel-software-rishikesh/', views.hotel_software_rishikesh, name="hotel_software_rishikesh"),
    path('hotel-software-mathura-vrindavan/', views.hotel_software_mathura_vrindavan, name="hotel_software_mathura_vrindavan"),
    path('hotel-software-prayagraj/', views.hotel_software_prayagraj, name="hotel_software_prayagraj"),
    path('hotel-software-puri/', views.hotel_software_puri, name="hotel_software_puri"),
    path('hotel-software-katra-vaishno-devi/', views.hotel_software_katra_vaishno_devi, name="hotel_software_katra_vaishno_devi"),
    path('hotel-software-nashik/', views.hotel_software_nashik, name="hotel_software_nashik"),

    path('hotel-channel-manager/', views.hotel_channel_manager, name="hotel_channel_manager"),

    path('hotel-pms-software/', views.hotel_pms_software, name="hotel_pms_software"),
    path('hotel-booking-engine/', views.hotel_booking_engine, name="hotel_booking_engine"),
    path('hotel-billing-software/', views.hotel_billing_software, name="hotel_billing_software"),
    path('list-hotel-on-makemytrip/', views.list_hotel_on_makemytrip, name="list_hotel_on_makemytrip"),
    path('list-hotel-on-booking-com/', views.list_hotel_on_booking_com, name="list_hotel_on_booking_com"),
    path('list-hotel-on-airbnb/', views.list_hotel_on_airbnb, name="list_hotel_on_airbnb"),

    # urls.py
    path('makemytrip-channel-manager/', views.makemytrip_channel_manager, name="makemytrip_channel_manager"),
    path('booking-com-channel-manager/', views.booking_com_channel_manager, name="booking_com_channel_manager"),
    path('goibibo-channel-manager/', views.goibibo_channel_manager, name="goibibo_channel_manager"),
    path('agoda-channel-manager/', views.agoda_channel_manager, name="agoda_channel_manager"),
    path('airbnb-channel-manager/', views.airbnb_channel_manager, name="airbnb_channel_manager"),
    path('homestay-management-software/', views.homestay_management_software, name="homestay_management_software"),
    path('resort-management-software/', views.resort_management_software, name="resort_management_software"),
    path('guest-house-management-software/', views.guest_house_management_software, name="guest_house_management_software"),
    path('boutique-hotel-software/', views.boutique_hotel_software, name="boutique_hotel_software"),
    path('service-apartment-management-software/', views.service_apartment_management_software, name="service_apartment_management_software"),
    

    # urls.py
    path('google-hotel-center-integration/', views.google_hotel_center_integration, name="google_hotel_center_integration"),
    path('google-free-booking-links-hotels/', views.google_free_booking_links_hotels, name="google_free_booking_links_hotels"),
    path('free-hotel-api-for-pms-companies/', views.free_hotel_api_for_pms_companies, name="free_hotel_api_for_pms_companies"),
    path('hotel-tech-partner-program-agencies/', views.hotel_tech_partner_program_agencies, name="hotel_tech_partner_program_agencies"),
    path('how-google-hotel-booking-works/', views.how_google_hotel_booking_works, name="how_google_hotel_booking_works"),
    path('benefits-of-google-hotel-integration/', views.benefits_of_google_hotel_integration, name="benefits_of_google_hotel_integration"),
    path('reduce-ota-commission-google-direct-bookings/', views.reduce_ota_commission_google_direct_bookings, name="reduce_ota_commission_google_direct_bookings"),
    path('google-hotel-integration-partner-india/', views.google_hotel_integration_partner_india, name="google_hotel_integration_partner_india"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'app.views.custom_404'