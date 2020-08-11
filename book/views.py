from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, TemplateView, FormView
from book.models import Book, Rate, RateTest
from .forms import RateForm


# Create your views here.
def home_view(request):
    context = {
        'books': Book.objects.all()
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


class BookRateView(TemplateView):
    model = Rate
    template_name = 'book/book_rate.html'


class BookRateFormView(FormView):
    model = RateTest
    template_name = 'book/book_rate_form.html'
    form_class = RateForm
    initial = {'key': 'value'}
    success_url = reverse_lazy('book-home')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(BookRateFormView, self).get_context_data(object_list=object_list, **kwargs)
    #     context['book'] = Book.objects.all()
    #     print(Book.objects.all())
    #     return context

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        print('get method')
        # book = get_object_or_404(Book, pk=self.kwargs.get("pk"))
        print(self.kwargs.get("pk"))
        print(self.kwargs)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.user = self.request.user
            book = get_object_or_404(Book, pk=self.kwargs.get("pk"))
            # print(book)
            form.instance.book = book
            # print(book)
            messages.success(request=self.request, message="Voted!")
            form.save()
            return redirect(reverse('book-home'))
        else:
            # messages.error(request=self.request, message=form.errors, extra_tags='danger')
            messages.error(request=self.request, message='Rate test with this Book and User already exists.',
                           extra_tags='danger')
            # return render(request, self.template_name, {'form':form})
            return redirect(reverse('book-home'))


def about_view(request):
    return render(request, 'book/about.html', {"title": "About"})


def rate_view(request):
    rate = Rate.objects.all().values()
    # print(rate)
    book_id_set = {elem['book_id'] for elem in rate}
    # print(book_id_set)
    book_rates_dict = {}
    for elem in book_id_set:
        book_rates_dict[elem] = []
    # print(book_rates_dict)
    for elem in rate:
        if elem['book_id'] in book_rates_dict.keys():
            book_rates_dict[elem['book_id']] += [elem['rate']]
    print(book_rates_dict)
    for key, value in book_rates_dict.items():
        book_rates_dict[key] = sum(value) / len(value)
    print(book_rates_dict)

    return render(request, 'book/book_rate_func.html', {'book_rates_dict': book_rates_dict})
