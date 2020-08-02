from django.shortcuts import render
from django.views.generic import DetailView
from book.models import Book
from .forms import RateForm

# Create your views here.
def home_view(request):
    form = RateForm(request.POST)
    context = {
        'books':Book.objects.all()
    }
    return render(request, 'book/home.html', context)

class BookDetailView(DetailView):
    model = Book

def about_view(request):
    return render(request, 'book/about.html',{"title":"About"})