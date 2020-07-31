from django.urls import path
from . import views as bookviews

urlpatterns = [
    path('', bookviews.home_view, name='book-home'),
    path('about/', bookviews.about_view, name='book-about'),
]