from django.shortcuts import render
from django.views.generic import DetailView, ListView
from book.models import Book
from .forms import RateForm

# Create your views here.
def home_view(request):
    form = RateForm(request.POST)
    context = {
        'books':Book.objects.all()
    }
    return render(request, 'book/home.html', context)

class BookListView(ListView):
    model = Book
    template_name = 'book/home.html'
    context_object_name = 'books'
    ordering = ['title']
    paginate_by = 5

class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookDetailView, self).get_context_data(object_list=object_list, **kwargs)
        form = RateForm()
        context.update({'form':form})
        return context

def about_view(request):
    return render(request, 'book/about.html',{"title":"About"})