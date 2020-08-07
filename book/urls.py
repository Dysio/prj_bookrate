from django.urls import path
from .views import BookListView, BookDetailView, RatePartialView, BookRateView
from . import views as bookviews

urlpatterns = [
    path('', BookListView.as_view(), name='book-home'),
    path('book/<pk>/', BookDetailView.as_view(), name='book-detail'),
    # path('book/<pk>/rate', RatePartialView.as_view(), name='book-detail-rate'),
    path('book/<pk>/rate', BookRateView.as_view(), name='rate-partial-view'),
    path('about/', bookviews.about_view, name='book-about'),
]

