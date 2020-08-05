from django.urls import path, include
from rest_framework import routers

from webapp.views import (BookViewset, CategoryViewset, BookCategoryListView, OrderBook,
                          OrderUpdateBook)

router = routers.DefaultRouter()
router.register(r'books', BookViewset, basename='books')
router.register(r'categories', CategoryViewset, basename='categories')


app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
    path('books/category/<int:pk>/', BookCategoryListView.as_view(), name='books_by_category'),
    path('order/book/', OrderBook.as_view(), name='order_book'),
    path('order/book/<int:pk>/edit/', OrderUpdateBook.as_view(), name='order_update_book')
]
