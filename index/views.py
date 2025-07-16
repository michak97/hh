from django.shortcuts import render
from news.models import News
from index.models import Teaser, TeaserIcon, IndexCard
from datetime import datetime
from articles.models import Category, Article
from administration.models import Logo
from django.utils.safestring import mark_safe

def index(request):
    teaser = Teaser.objects.all().first()
    articles= Article.objects.filter(draft=False, is_published=True, end_date__date__lte=datetime.now())
    categories = Category.objects.all()
    indexcards = IndexCard.objects.all()
    for card in indexcards:
        card.svg=card.image.svg.open('r').read()
    logo = Logo.objects.first()
    news = News.objects.all()
    return render(request, 'index/index.html', {"articles":articles, "categories": categories, "teaser": teaser, "logo": logo, "indexcards": indexcards, "news": news})

# Create your views here.
