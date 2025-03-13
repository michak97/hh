from django.db import models
from django.contrib.auth.models import User


class Teaser(models.Model):
    image_file = models.ImageField(upload_to="media/teaser/images/", verbose_name="Bild")
    text = models.CharField(max_length=64, verbose_name="Text")
    description = models.CharField(max_length=256, verbose_name="Beschreibung")

    def __str__(self):
        return self.description

class IndexHeader(models.Model):
    content = models.CharField(max_length=64)

    def __str__(self):
        return self.content

class TeaserIcon(models.Model):
    title = models.CharField(max_length=64, verbose_name="Titel")
    svg = models.FileField(upload_to="media/teaser/icons", verbose_name="svg_datei")

    def __str__(self):
        return self.title

class IndexCard(models.Model):
    image = models.ForeignKey(TeaserIcon, on_delete=models.PROTECT)
    text = models.CharField(max_length=2048)

# Create your models here.
