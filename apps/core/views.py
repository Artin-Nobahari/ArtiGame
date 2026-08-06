from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about_us(request):
    return render(request, "core/about-us.html")

def contact_us(request):
    return render(request, "core/contact-us.html")