from django.shortcuts import render
from news.models import Article
from index.models import Teaser, IndexHeader, IndexText, Content

def index(request):
    teaser = Teaser.objects.all()
    header = IndexHeader.objects.all()
    indextexts = IndexText.objects.all()
    content = Content.objects.filter(draft=False, is_published=True)
    articles=Article.objects.filter(draft=False, is_published=True)
    return render(request, 'index/index.html', {"articles":articles, "header": header, "indextexts": indextexts, "content": content})

# Create your views here.
