from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from PIL import Image 

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


class Client(models.Model):
    logo = models.ImageField(upload_to="clients/", max_length=100)

    def __str__(self) -> str:
        return f"Client {self.id + 1}"

    def save(self, *args, **kwargs):
        super(Client, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200,200)
            img.thumbnail(output_size)
            img.save(self.image.path)
