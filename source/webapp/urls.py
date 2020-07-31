from django.urls import path, include
from rest_framework import routers

from webapp.views import BookViewset

router = routers.DefaultRouter()
router.register(r'books', BookViewset, basename='books')

app_name='api_v1'

urlpatterns = [
    path('', include(router.urls))
]
