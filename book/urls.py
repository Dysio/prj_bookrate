from django.urls import path
from .views import BookListView,BookDetailView
from . import views as bookviews

urlpatterns = [
    path('', BookListView.as_view(), name='book-home'),
    path('book/<pk>/', BookDetailView.as_view(), name='book-detail'),
    path('about/', bookviews.about_view, name='book-about'),
]