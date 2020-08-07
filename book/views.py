from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, FormView
from book.models import Book, Rate
from .forms import RateForm

# Create your views here.
def home_view(request):
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookListView, self).get_context_data(object_list=object_list, **kwargs)
        context['rates'] = Rate.objects.all()
        return context

class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookDetailView, self).get_context_data(object_list=object_list, **kwargs)
        form = RateForm()
        context.update({'form':form})
        context['rates'] = Rate.objects.all()
        return context

class BookRateView(TemplateView):
    model = Rate
    template_name = 'book/book_rate.html'

class BookRateFormView(FormView):
    model = Rate
    template_name = 'book/book_rate_form.html'
    form_class = RateForm
    success_url = reverse_lazy('book-home')

class RatePartialView(DetailView):
    model = Rate
    # template_name = 'book/rate_partial_view.html'
    # context_object_name = 'rates'

    # def get_context_data(self, **kwargs):
    #     result = kwargs['arg1'] + kwargs['arg2']
    #     kwargs['result'] = result
    #     return super(RatePartialView, self).get_context_data(**kwargs)


def about_view(request):
    return render(request, 'book/about.html',{"title":"About"})