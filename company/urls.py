from core.views import (
    home,
    contact,
    about,
    tax_info,
    tax_tools,
    create_testimonial
)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('tax-info/', tax_info, name="tax_info"),
    path('tax-tools/', tax_tools, name="tax_tools"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('leave-a-review/', create_testimonial, name="create_testimonial"),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]

admin.site.site_header = "DKC Consulting Admin"
admin.site.site_title = "DKC Consulting Admin Portal"
admin.site.index_title = "Welcome to DKC Consulting Portal"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
