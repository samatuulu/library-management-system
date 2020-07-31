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
