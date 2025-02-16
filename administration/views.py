from django.shortcuts import render

def login_view(request):
    return render(request, 'administration/login.html', {})

# Create your views here.
