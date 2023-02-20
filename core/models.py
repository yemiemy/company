from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=254)
    link = models.URLField(max_length=508)
    created_at = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"Testimonial by {self.name}"


class TaxInformation(models.Model):
    title = models.CharField(max_length=250)
    body = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class TaxTool(models.Model):
    title = models.CharField(max_length=250)
    body = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
