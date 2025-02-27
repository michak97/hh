from django.shortcuts import render
from articles.models import Article, Category

def read_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    categories = Category.objects.all()
    return render(request, "articles/article.html", {'article': article, 'categories': categories})

def read_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    categories = Category.objects.all()
    return render(request, "category/category.html", {'category': category, 'categories': categories})
# Create your views here.
