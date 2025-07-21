from django.shortcuts import render
from django.http import HttpResponse
from news.models import News
from articles.models import Category

def detail(request, news_id):
    article = News.objects.get(pk=news_id)
    categories = Category.objects.all()
    try:
        template=article.template.template
    except Exception as e:
        template="articles/article.html"
    further_articles = News.objects.exclude(pk=news_id).filter(is_published=True).order_by('?')[:3]
    news = News.objects.all()
    return render(request, template, {'article': article, 'categories': categories, 'further_articles': further_articles, 'news': news})

# Create your views here.
