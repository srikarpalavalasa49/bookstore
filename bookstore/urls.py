# bookstore/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('authors/', views.author_list, name='author_list'),
    path('', views.home_view, name='home'),
    # Other URL patterns for your app views go here
]
