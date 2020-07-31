from rest_framework import serializers

from webapp.models import Book, BookAuthor


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=False, queryset=BookAuthor.objects.all())

    class Meta:
        model = Book
        fields = ('id', 'author', 'title', 'description', 'image', 'status')
