from django.db import models
from tinymce import models as tinymce

class Logo(models.Model):
    image_file=models.ImageField(upload_to='logo/', verbose_name="Bilddatei", blank=True, null=True)
    svg_file=models.FileField(upload_to='logo/', verbose_name="Vektorgrafik", blank=True, null=True)

class PrivacyPolicy(models.Model):
    text = tinymce.HTMLField(max_length=100000, verbose_name="Datenschutzerklärung")

    def __str__(self):
        return "Datenschutzerklärung"

class Imprint(models.Model):
    text = tinymce.HTMLField(max_length=100000, verbose_name="Datenschutzerklärung")

    def __str__(self):
        return "Impressum"
