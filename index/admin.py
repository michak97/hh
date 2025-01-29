from django.contrib import admin
from .models import Category, Content, Teaser, TeaserIcon, IndexCard

admin.site.register(TeaserIcon)
admin.site.register(Teaser)
admin.site.register(Category)
admin.site.register(Content)
admin.site.register(IndexCard)
# Register your models here.
