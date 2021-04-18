from django.urls import path
from .views import BookList, BookDetails

urlpatterns = [
    path('', BookList.as_view()),
    path('<int:id>/', BookDetails.as_view()),
]
