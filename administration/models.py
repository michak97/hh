from django.db import models

class Logo(models.Model):
    image_file=models.ImageField(upload_to='media/static/img/logo/', verbose_name="Bilddatei", blank=True, null=True)
    svg_file=models.FileField(upload_to='media/static/svg/logo/', verbose_name="Vektorgrafik", blank=True, null=True)
