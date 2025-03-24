from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    path('', views.index,name="index"),
    path('price/', views.price,name="price"),
    path('about/', views.about,name="about"),
    path('channelmanager/', views.channelmanager,name="channelmanager"),
    path('PMS/', views.PMS,name="PMS"),
    path('addfreedemo/', views.index,name="addfreedemo"),
    path('terms/', views.terms,name="terms"),
    path('privcy/', views.privcy,name="privcy"),
    path('refund/', views.refund,name="refund"),
    path('website/', views.website,name="website"),
    path('proxy-create-demo/', views.forward_to_live_api, name='proxy_create_demo'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'app.views.custom_404'