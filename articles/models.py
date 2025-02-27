from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    title= models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        main_article = Article.objects.filter(category=self, main_article=True).first()
        return reverse('read_article', kwargs={"article_id": main_article.pk})

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete = models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Titel")
    content = models.CharField(max_length=2048, verbose_name="Inhalt")
    pub_date = models.DateTimeField(verbose_name="Veröffentlichungsdatum")
    end_date = models.DateTimeField(verbose_name="Ablaufdatum")
    is_published = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)
    main_article = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('read_article', kwargs={"article_id": self.pk})

# Create your models here.
