# bookstore/views.py
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Book, Author

@cache_page(60 * 5)  # Cache the page for 5 minutes
def home_view(request):
    return render(request, 'bookstore/index.html')

@cache_page(60 * 5)  # Cache the page for 5 minutes
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookstore/book_list.html', {'books': books})

@cache_page(60 * 5)  # Cache the page for 5 minutes
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'bookstore/author_list.html', {'authors': authors})
