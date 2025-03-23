from django.shortcuts import render
from administration.models import PrivacyPolicy, Imprint
from articles.models import Article, Category

def login_view(request):
    return render(request, 'administration/login.html', {})

def read_privacy_policy(request):
    categories = Category.objects.all()
    return render(request, 'administration/privacy_policy.html', {"policy": PrivacyPolicy.objects.last(), "categories": categories})

def read_imprint(request):
    categories = Category.objects.all()
    return render(request, 'administration/imprint.html', {"imprint": Imprint.objects.last(), 'categories': categories})
# Create your views here.
