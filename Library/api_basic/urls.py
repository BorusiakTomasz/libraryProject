from django.urls import path
from .views import article_detail, ArticleList

urlpatterns = [
    path('article/', ArticleList.as_view()),
    path('detail/<int:pk>/', article_detail),
]
