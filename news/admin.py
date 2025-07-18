from django.contrib import admin
from django.db import models
from .models import News, NewsTemplate

admin.site.register(News)
admin.site.register(NewsTemplate)

# Register your models here.
