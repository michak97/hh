from django.shortcuts import render
from administration.models import PrivacyPolicy, Imprint
from articles.models import Article, Category
from news.models import News

def login_view(request):
    return render(request, 'administration/login.html', {})

def read_privacy_policy(request):
    categories = Category.objects.all()
    news = News.objects.all()
    return render(request, 'administration/privacy_policy.html', {"policy": PrivacyPolicy.objects.last(), "categories": categories, 'news': news})

def read_imprint(request):
    categories = Category.objects.all()
    news = News.objects.all()
    return render(request, 'administration/imprint.html', {"imprint": Imprint.objects.last(), 'categories': categories, 'news': news})
# Create your views here.
