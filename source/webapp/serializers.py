from rest_framework import serializers

from webapp.models import Book, BookAuthor, Category, Order, OrderBook


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


class OrderBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderBook
        fields = ('id', 'book', 'amount')


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    order_book = OrderBookSerializer(source='order_books', write_only=True)

    class Meta:
        model = Order
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'order_book')

    def create(self, validated_data):
        data = validated_data.pop('order_books')
        order = Order.objects.create(**validated_data)
        OrderBook.objects.create(order=order, **data)
        return order

    def update(self, instance, validated_data):
        instance = self.save_data(instance, validated_data)
        order = validated_data.get('order_books')
        OrderBook.objects.filter(order=instance.id).update(book=order['book'], amount=order['amount'])
        return instance

    def save_data(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        order_book = OrderBook.objects.get(order=representation['id'])
        representation['book'] = order_book.book.title
        representation['amount'] = order_book.amount
        return representation
