from django.contrib import admin
from .models import Book, Rate

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','year']

class RateAdmin(admin.ModelAdmin):
    list_display = ['book','user','rate']

admin.site.register(Book, BookAdmin)
admin.site.register(Rate, RateAdmin)
