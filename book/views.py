from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, TemplateView, FormView
from book.models import Book, Rate, RateTest
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
    model = RateTest
    template_name = 'book/book_rate_form.html'
    form_class = RateForm
    initial = {'key':'value'}
    success_url = reverse_lazy('book-home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookRateFormView, self).get_context_data(object_list=object_list, **kwargs)
        context['book'] = Book.objects.all()
        print(Book.objects.all())
        return context

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            messages.success(request=self.request, message="Voted!")
            form.save()
            return redirect(reverse('book-home'))
        return render(request, self.template_name, {'form':form})



def about_view(request):
    return render(request, 'book/about.html',{"title":"About"})