from django.db import models
from django.contrib.auth.models import User


class Teaser(models.Model):
    image_file = models.ImageField(upload_to="media/teaser/images/")
    text = models.CharField(max_length=64)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.description

class IndexHeader(models.Model):
    content = models.CharField(max_length=64)

    def __str__(self):
        return self.content

class TeaserIcon(models.Model):
    title = models.CharField(max_length=64)
    svg = models.FileField(upload_to="media/teaser/icons")

    def __str__(self):
        return self.title

class IndexCard(models.Model):
    image = models.ForeignKey(TeaserIcon, on_delete=models.PROTECT)
    text = models.CharField(max_length=2048)

# Create your models here.
