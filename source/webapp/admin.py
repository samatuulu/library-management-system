from django.contrib import admin

from webapp.models import BookAuthor, Book, Category, Feedback

admin.site.register(BookAuthor)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Feedback)