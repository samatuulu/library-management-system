from rest_framework import viewsets

from webapp.models import Book, BookAuthor
from webapp.serializers import BookSerializer


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
