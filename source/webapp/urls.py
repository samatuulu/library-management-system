from django.urls import path, include
from rest_framework import routers

from webapp.views import BookViewset, CategoryViewset

router = routers.DefaultRouter()
router.register(r'books', BookViewset, basename='books')
router.register(r'categories', CategoryViewset, basename='categories')


app_name='api_v1'

urlpatterns = [
    path('', include(router.urls))
]
