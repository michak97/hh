from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete = models.PROTECT)
    title = models.CharField(max_length=200, verbose_name="Titel")
    content = models.CharField(max_length=2048, verbose_name="Inhalt")
    pub_date = models.DateTimeField(verbose_name="Veröffentlichungsdatum")
    end_date = models.DateTimeField(verbose_name="Ablaufdatum")
    is_published = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title


