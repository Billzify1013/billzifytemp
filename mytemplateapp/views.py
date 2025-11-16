from django.shortcuts import render

# Create your views here.
def indexnew(request):
    print('my app run')
    return render(request,'mytemplateapp/index.html')