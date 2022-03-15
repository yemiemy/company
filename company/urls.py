from core.views import home, contact, services, faq
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('services/', services, name="services"),
    path('faq/', faq, name="faq")
]
