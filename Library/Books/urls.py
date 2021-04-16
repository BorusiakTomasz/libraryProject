from django.urls import path
from .views import ArticleList, ArticleDetails

urlpatterns = [
    path('', ArticleList.as_view()),
    path('<int:id>/', ArticleDetails.as_view()),
]
