from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title= models.CharField(max_length=200)

class Content(models.Model):
    writer = models.ForeignKey(User, on_delete = models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Titel")
    content = models.CharField(max_length=2048, verbose_name="Inhalt")
    pub_date = models.DateTimeField(verbose_name="Veröffentlichungsdatum")
    end_date = models.DateTimeField(verbose_name="Ablaufdatum")
    is_published = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

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
