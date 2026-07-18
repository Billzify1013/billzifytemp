from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def index(request):
    return render(request,'index.html')


import requests
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib import messages

@csrf_exempt  # Optional: Handle CSRF in production
def forward_to_live_api(request):
    if request.method == "POST":
        # Collect form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        businessname = request.POST.get("businessname")

        # Prepare data for the external API
        payload = {
            "name": name,
            "email": email,
            "phone": phone,
            "businessname": businessname,
        }
        
        # Call the live API
        api_url = "https://live.billzify.com/create_demo/"
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(api_url, json=payload, headers=headers)

            # Check if the API call was successful
            if response.status_code == 200:
                messages.success(request, "Your demo request was successfully submitted!")
            else:
                messages.error(request, f"Failed to submit demo request. API responded with status {response.status_code}.")
        except requests.RequestException as e:
            messages.error(request, f"An error occurred: {str(e)}")
        
        # Redirect to the same page or a success page
        return redirect("index")  # Replace with your success page URL name

    return redirect("index") 


def custom_404(request, exception):
    return render(request, '404.html', status=404)

def privcy(request):
    return render(request,'privcy.html')

def refund(request):
    return render(request,'refund.html')

def terms(request):
    return render(request,'terms.html')

def price(request):
    return render(request,'pricing.html')

def about(request):
    return render(request,'about.html')

def website(request):
    return render(request,'websitefree.html')

def channelmanager(request):
    return render(request,'channel.html')

def PMS(request):
    return render(request,'pms.html')

def BookingEngine(request):
    return render(request,'be.html')

def blog(request):
    return render(request,'blog.html')

def blogcmguide(request):
    return render(request,'channel-manager-guide.html')

def blogdyprice(request):
    return render(request,'dynamic-pricing-strategy.html')

def cmapi(request):
    return render(request,'cmapi.html')


class RobotsTxtView(TemplateView):
    template_name = "robots.txt"
    content_type = "text/plain"

def delete_account_view(request):
    return render(request, 'delete_account.html')

def bloggoogleranking(request):
    return render(request, 'hotel-google-ranking.html')

def mobileapp(request):
    return render(request, 'app.html')

def channel_manager_price_india(request):
    return render(request,'channel-manager-price-india.html')

def best_channel_manager_small_hotels(request):
    return render(request,'best-channel-manager-small-hotels.html')

def channel_manager_vs_pms(request):
    return render(request,'channel-manager-vs-pms.html')


def hotel_software_ujjain(request):
    return render(request, 'hotel-software-ujjain.html')

def hotel_software_indore(request):
    return render(request, 'hotel-software-indore.html')

def hotel_software_jaipur(request):
    return render(request, 'hotel-software-jaipur.html')

def hotel_software_goa(request):
    return render(request, 'hotel-software-goa.html')

def hotel_software_varanasi(request):
    return render(request, 'hotel-software-varanasi.html')

def hotel_software_udaipur(request):
    return render(request, 'hotel-software-udaipur.html')


def hotel_software_ayodhya(request):
    return render(request, 'hotel-software-ayodhya.html')

def hotel_software_khatu_shyam(request):
    return render(request, 'hotel-software-khatu-shyam.html')

def hotel_software_somnath(request):
    return render(request, 'hotel-software-somnath.html')

def hotel_software_kolkata(request):
    return render(request, 'hotel-software-kolkata.html')

def hotel_software_vijayawada(request):
    return render(request, 'hotel-software-vijayawada.html')

def hotel_software_nandyal(request):
    return render(request, 'hotel-software-nandyal.html')


def hotel_software_tirupati(request):
    return render(request, 'hotel-software-tirupati.html')

def hotel_software_shirdi(request):
    return render(request, 'hotel-software-shirdi.html')

def hotel_software_amritsar(request):
    return render(request, 'hotel-software-amritsar.html')

def hotel_software_haridwar(request):
    return render(request, 'hotel-software-haridwar.html')

def hotel_software_rishikesh(request):
    return render(request, 'hotel-software-rishikesh.html')

def hotel_software_mathura_vrindavan(request):
    return render(request, 'hotel-software-mathura-vrindavan.html')

def hotel_software_prayagraj(request):
    return render(request, 'hotel-software-prayagraj.html')

def hotel_software_puri(request):
    return render(request, 'hotel-software-puri.html')

def hotel_software_katra_vaishno_devi(request):
    return render(request, 'hotel-software-katra-vaishno-devi.html')

def hotel_software_nashik(request):
    return render(request, 'hotel-software-nashik.html')

def hotel_channel_manager(request):
    return render(request, 'hotel-channel-manager.html')

def hotel_pms_software(request):
    return render(request, 'hotel-pms-software.html')

def hotel_booking_engine(request):
    return render(request, 'hotel-booking-engine.html')

def hotel_billing_software(request):
    return render(request, 'hotel-billing-software.html')

def list_hotel_on_makemytrip(request):
    return render(request, 'list-hotel-on-makemytrip.html')

def list_hotel_on_booking_com(request):
    return render(request, 'list-hotel-on-booking-com.html')

def list_hotel_on_airbnb(request):
    return render(request, 'list-hotel-on-airbnb.html')



# views.py
def makemytrip_channel_manager(request):
    return render(request, 'makemytrip-channel-manager.html')

def booking_com_channel_manager(request):
    return render(request, 'booking-com-channel-manager.html')

def goibibo_channel_manager(request):
    return render(request, 'goibibo-channel-manager.html')

def agoda_channel_manager(request):
    return render(request, 'agoda-channel-manager.html')

def airbnb_channel_manager(request):
    return render(request, 'airbnb-channel-manager.html')

def homestay_management_software(request):
    return render(request, 'homestay-management-software.html')

def resort_management_software(request):
    return render(request, 'resort-management-software.html')

def guest_house_management_software(request):
    return render(request, 'guest-house-management-software.html')

def boutique_hotel_software(request):
    return render(request, 'boutique-hotel-software.html')

def service_apartment_management_software(request):
    return render(request, 'service-apartment-management-software.html')