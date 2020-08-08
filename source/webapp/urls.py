from django.urls import path, include
from rest_framework import routers

from webapp.views import (BookViewset, CategoryViewset, BookCategoryListView,
                          OrderBookView, OrderUpdateBook, OrderDeleteBook, OrderBookDetail,
                          FeedbackViewset)

router = routers.DefaultRouter()
router.register(r'books', BookViewset, basename='books')
router.register(r'categories', CategoryViewset, basename='categories')
router.register(r'feedback', FeedbackViewset, basename='feedback')


app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
    path('books/category/<int:pk>/', BookCategoryListView.as_view(), name='books_by_category'),
    path('order/book/', OrderBookView.as_view(), name='order_book'),
    path('order/book/<int:pk>/', OrderBookDetail.as_view(), name='order_book_detail'),
    path('order/book/<int:pk>/edit/', OrderUpdateBook.as_view(), name='order_update_book'),
    path('order/book/<int:pk>/delete/', OrderDeleteBook.as_view(), name='order_book_delete'),
]
