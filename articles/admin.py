from django.contrib import admin
from articles.models import Category, Article, ArticleTemplate

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(ArticleTemplate)
# Register your models here.
