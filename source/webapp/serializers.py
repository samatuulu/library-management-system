from rest_framework import serializers

from webapp.models import Book, BookAuthor, Category


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=False, queryset=BookAuthor.objects.all())
    category = serializers.PrimaryKeyRelatedField(many=False, queryset=Category.objects.all())

    class Meta:
        model = Book
        fields = ('id', 'author', 'title', 'description', 'image', 'status', 'category')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')
