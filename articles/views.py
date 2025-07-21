from django.shortcuts import render
from articles.models import Article, Category
from news.models import News

def read_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    categories = Category.objects.all()
    try:
        template=article.template.template
    except Exception as e:
        template="articles/article.html"
    further_articles = Article.objects.exclude(pk=article_id).filter(is_published=True).order_by('?')[:3]
    news = News.objects.all()
    return render(request, template, {'article': article, 'categories': categories, 'further_articles': further_articles, 'news': news})

def read_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    categories = Category.objects.all()
    return render(request, "category/category.html", {'category': category, 'categories': categories})
