from django.urls import path
from . import views

urlpatterns = [
    path("/category/<category_id>", views.read_category, name="read_category"),
    path("/article/<article_id>", views.read_article, name="read_article"),

]
