from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404

from webapp.models import Book, Category, Order
from webapp.serializers import BookSerializer, CategorySerializer, OrderCreateUpdateSerializer


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookCategoryListView(generics.ListAPIView):
    queryset = Category
    serializer_class = BookSerializer

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        books_by_category = Book.objects.filter(category__name=category)
        return books_by_category


class OrderBook(generics.CreateAPIView):
    queryset = Order
    serializer_class = OrderCreateUpdateSerializer


class OrderUpdateBook(generics.UpdateAPIView):
    queryset = Order
    serializer_class = OrderCreateUpdateSerializer
