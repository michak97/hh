from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="article_detail"),
    path("imprint/", views.read_imprint, name="imprint_detail"),
    path("privacy_policy/", views.read_privacy_policy, name="privacy_policy_detail")
]
