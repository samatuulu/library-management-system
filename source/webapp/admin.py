from django.contrib import admin

from webapp.models import BookAuthor, Book, Category, Feedback, Order, OrderBook


class OrderBookInline(admin.TabularInline):
    model = OrderBook
    fields = ('book', 'amount')
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('first_name', )
    inlines = (OrderBookInline, )


admin.site.register(BookAuthor)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Feedback)
admin.site.register(Order, OrderAdmin)
