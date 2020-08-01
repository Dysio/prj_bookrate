from django.shortcuts import render
from .models import Book

# Create your views here.
def home_view(request):
    context = {
        'books':Book.objects.all()
    }
    return render(request, 'book/home.html', context)

def about_view(request):
    return render(request, 'book/about.html',{"title":"About"})