from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'book/home.html')

def about_view(request):
    return render(request, 'book/about.html',{"title":"About"})