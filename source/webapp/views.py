from rest_framework import viewsets

from webapp.models import Book, Category
from webapp.serializers import BookSerializer, CategorySerializer


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
