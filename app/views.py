from django.shortcuts import render

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