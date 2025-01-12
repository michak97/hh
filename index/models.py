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
    image_file = models.FileField(upload_to="teaser/")
    text = models.CharField(max_length=64)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.description

class IndexHeader(models.Model):
    content = models.CharField(max_length=64)

    def __str__(self):
        return self.content

class IndexText(models.Model):
    content = models.CharField(max_length=1024)

    def __str__(self):
        return f"{str(self.content)[0:27:1]}..."

# Create your models here.
