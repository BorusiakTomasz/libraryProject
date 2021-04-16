from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleList, ArticleDetails, GenericAPIView, ArticleViewSet

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('', ArticleList.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/', GenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]
