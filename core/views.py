from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.html")

def services(request):
    return render(request, "services.html")
    
def contact(request):
    return render(request, "contact.html")


def faq(request):
    return render(request, "faq.html")

def page404(request):
    return render(request, "404.html")