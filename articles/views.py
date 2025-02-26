from django.shortcuts import render

def read_article(request):
    articles = Article.objects.all()
# Create your views here.
