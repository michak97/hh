from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce

class News(models.Model):
    writer = models.ForeignKey(User, on_delete = models.PROTECT, verbose_name="Autor")
    title = models.CharField(max_length=200, verbose_name="Titel")
    content = tinymce.HTMLField(max_length=2048, verbose_name="Inhalt")
    pub_date = models.DateTimeField(verbose_name="Veröffentlichungsdatum")
    end_date = models.DateTimeField(verbose_name="Ablaufdatum")
    is_published = models.BooleanField(default=False, verbose_name="öffentlich")
    draft = models.BooleanField(default=False, verbose_name="Entwurf")

    def __str__(self):
        return self.title


