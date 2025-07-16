from django.contrib import admin
from articles.models import Category, Article, ArticleTemplate, ArticleImage

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1
    verbose_name = "Bild"
    verbose_name_plural = "Bilder"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'category', 'pub_date', 'is_published', 'draft')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'draft', 'category')
    date_hierarchy = 'pub_date'
    inlines = [ArticleImageInline]


admin.site.register(Category)
admin.site.register(ArticleTemplate)
admin.site.register(Article, ArticleAdmin)
# Register your models here.
