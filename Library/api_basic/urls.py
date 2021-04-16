from django.urls import path
from .views import ArticleList, ArticleDetails

urlpatterns = [
    path('article/', ArticleList.as_view()),
    path('detail/<int:pk>/', ArticleDetails.as_view()),
]
