from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from tinymce import models as tinymce
from django.utils.html import strip_tags

class NewsTemplate(models.Model):
    title=models.CharField(max_length=64, verbose_name="Name")
    template=models.CharField(max_length=128, verbose_name="TemplateDirectory")

    def __str__(self):
        return self.title

class News(models.Model):
    writer = models.ForeignKey(User, on_delete = models.PROTECT, verbose_name="Autor")
    title = models.CharField(max_length=200, verbose_name="Titel")
    content = tinymce.HTMLField(max_length=2048, verbose_name="Inhalt")
    pub_date = models.DateTimeField(verbose_name="Veröffentlichungsdatum")
    end_date = models.DateTimeField(verbose_name="Ablaufdatum")
    is_published = models.BooleanField(default=False, verbose_name="öffentlich")
    draft = models.BooleanField(default=False, verbose_name="Entwurf")
    template = models.ForeignKey(NewsTemplate, on_delete=models.CASCADE, verbose_name="Design", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={"news_id": self.pk})

    def stripped_content(self):
        return strip_tags(self.content)
