from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Book
from .serializers import BookSerializer

IMPORT_URL = 'https://www.googleapis.com/books/v1/volumes?q=war'


# Create your views here.


class BookList(APIView):
    def get(self, request):
        articles = Book.objects.all()
        serializer = BookSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetails(APIView):
    def get_object(self, id=None):
        try:
            return Book.objects.get(id=id)

        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id=None):
        article = self.get_object(id)
        serializer = BookSerializer(article)
        return Response(serializer.data)

    def put(self, request, id=None):
        article = self.get_object(id)
        serializer = BookSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
