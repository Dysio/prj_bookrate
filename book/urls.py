from django.urls import path
from .views import BookListView, BookDetailView, BookRateView, BookRateFormView
from . import views as bookviews

urlpatterns = [
    path('', BookListView.as_view(), name='book-home'),
    path('book/<pk>/', BookDetailView.as_view(), name='book-detail'),
    # path('book/<pk>/rate', RatePartialView.as_view(), name='book-detail-rate'),
    path('bookrate/', BookRateView.as_view(), name='book-rate'),
    path('bookratefunc/', bookviews.rate_view, name='book-rate-func'),
    path('bookrateform/', BookRateFormView.as_view(), name='book-rate-form'),
    path('about/', bookviews.about_view, name='book-about'),
]

