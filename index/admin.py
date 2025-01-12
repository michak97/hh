from django.contrib import admin
from .models import Category, Content, Teaser, IndexText, IndexHeader

admin.site.register(Teaser)
admin.site.register(IndexText)
admin.site.register(IndexHeader)
admin.site.register(Category)
admin.site.register(Content)
# Register your models here.
