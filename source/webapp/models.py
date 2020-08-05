from django.db import models


class BookAuthor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Book author')

    def __str__(self):
        return self.name


STATUS_CHOICES = (
    ('available', 'Available'),
    ('booked', 'Booked')
)


class Book(models.Model):
    author = models.ForeignKey('webapp.BookAuthor', related_name='book_author',
                               on_delete=models.CASCADE, verbose_name='Book author')
    title = models.CharField(max_length=200, verbose_name='Book title')
    description = models.TextField(max_length=1000, verbose_name='Book description')
    image = models.ImageField(upload_to='images') # one image for each books
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0],
                              verbose_name='Book status')
    slug = models.SlugField(max_length=255, blank=True, null=True) # for future functionality
    category = models.ForeignKey('webapp.Category', on_delete=models.CASCADE, related_name='book_category',
                                 verbose_name='Book Category')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.author_id)} {self.title}"

    class Meta:
        ordering = ('-created_at',)


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Book category')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Order(models.Model):
    user = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL,
                             verbose_name='User', related_name='orders')
    first_name = models.CharField(max_length=100, verbose_name='Name', null=True, blank=True)
    last_name = models.CharField(max_length=100, verbose_name='Last name', null=True, blank=True)
    email = models.EmailField(max_length=50, verbose_name='Email', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='Phone')
    books = models.ManyToManyField('webapp.Book', through='OrderBook', through_fields=('order', 'book'),
                                   verbose_name='Orders', related_name='orders')

    def __str__(self):
        return str(self.first_name)


class OrderBook(models.Model):
    order = models.ForeignKey('webapp.Order', on_delete=models.CASCADE, verbose_name='Order',
                              related_name='order_books')
    book = models.ForeignKey('webapp.Book', on_delete=models.CASCADE, verbose_name='Book/s',
                             related_name='order_books')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.book.title)


RATE_CHOICES = (
    ('one', 1),
    ('two', 2),
    ('three', 3),
    ('four', 4),
    ('five', 5)
)


class Feedback(models.Model):
    book = models.ForeignKey('webapp.Book', on_delete=models.CASCADE, verbose_name='Book')
    user = models.ForeignKey('auth.User', related_name='book_feedback', on_delete=models.CASCADE,
                             null=True, blank=True, verbose_name='User')
    book_feedback = models.TextField(max_length=1000, verbose_name='Feedback')
    rate = models.CharField(max_length=10, choices=RATE_CHOICES, verbose_name='Book rate')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_feedback

    class Meta:
        ordering = ('-created_at',)
