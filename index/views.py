from django.shortcuts import render
from news.models import Article
from index.models import Teaser, Content, TeaserIcon, IndexCard
from administration.models import Logo
from django.utils.safestring import mark_safe

def index(request):
    teaser = Teaser.objects.all().first()
    content = Content.objects.filter(draft=False, is_published=True)
    articles=Article.objects.filter(draft=False, is_published=True)
    indexcards = IndexCard.objects.all()
    for card in indexcards:
        card.svg=card.image.svg.open('r').read()
    logo = Logo.objects.first()
    return render(request, 'index/index.html', {"articles":articles, "content": content, "teaser": teaser, "logo": logo.svg_file.open('r').read(), "indexcards": indexcards})

# Create your views here.
