from django.shortcuts import render
from core.models import Testimonial, New, TaxInformation, TaxTool
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

def home(request):
    context = {
        'home_current': 'current',
        'testimonials': Testimonial.objects.order_by('-id'),
        'news': New.objects.order_by('-created_at')
    }
    return render(request, "index.html", context)

def services(request):
    return render(request, "services.html")
    
def about(request):
    return render(request, "about.html")
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "Anonymous Contact")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(name, email, phone, message)
        # send email here
        context = {
            'name':name,
            'email':email,
            'phone':phone,
            'message':message
        }
        body = render_to_string('emails/contact_form.html', context)
        plain_body = strip_tags(body)
        subject = f"DKC Consulting Contact Form <> Message from {name}"
        send_mail(
            subject, 
            plain_body, 
            'dkcconsultin@gmail.com', 
            ['dkcconsultin@gmail.com'],
            html_message=body
            )

        # Send back an automated email to contact(visitor)
        contexts = {
            'name':name,
        }
        reply = render_to_string('emails/contact_response.html', contexts)
        plain_reply = strip_tags(reply)
        send_mail(
            subject, 
            plain_reply, 
            'dkcconsultin@gmail.com', 
            [email], 
            html_message=reply
            )
    return render(request, "contact.html", {
        'contact_current': 'current', 
        'news': New.objects.order_by('-created_at')
    })

def about(request):
    return render(request, "about.html", {
        'about_current': 'current',
        'news': New.objects.order_by('-created_at')
    })

def tax_info(request):
    context = {
        'tax_info_current': 'current',
        'page_header': 'Tax Information',
        'news': New.objects.order_by('-created_at'),
        'object_list': TaxInformation.objects.order_by('-id')
    }
    return render(request, "tax_services.html", context)

def tax_tools(request):
    context = {
        'tax_tools_current': 'current',
        'page_header': 'Tax Tools',
        'news': New.objects.order_by('-created_at'),
        'object_list': TaxTool.objects.order_by('-id')
    }
    return render(request, "tax_services.html", context)


def create_testimonial(request):
    if request.method == "POST":
        name = request.POST.get("name", "Anonymous Reviewer")
        message = request.POST.get("message")
        if name and message:
            Testimonial.objects.create(name=name, review=message)
        print(name, message)
    return render(request, "testimonial.html", {
        'news': New.objects.order_by('-created_at')
    })


def faq(request):
    return render(request, "faq.html")

def page404(request):
    return render(request, "404.html")