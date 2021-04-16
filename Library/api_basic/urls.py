from django.urls import path
from .views import ArticleList, ArticleDetails, GenericAPIView

urlpatterns = [
    path('', ArticleList.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/', GenericAPIView.as_view()),
]
