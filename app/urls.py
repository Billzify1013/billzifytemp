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
    path('proxy-create-demo/', views.forward_to_live_api, name='proxy_create_demo'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, 
         name='django.contrib.sitemaps.views.sitemap'),

    path('robots.txt', RobotsTxtView.as_view(), name='robots'),
    path('delete-account/', views.delete_account_view, name='delete_account_view'),
    path('blog/hotel-google-ranking/', views.bloggoogleranking, name="bloggoogleranking"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'app.views.custom_404'