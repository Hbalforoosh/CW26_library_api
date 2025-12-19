from django.urls import path
from .views import AuthorListCreateView, AuthorDetailView, CategoryListCreateView, CategoryDetailView, BookListCreateView, BookDetailView
urlpatterns = [
    path('authors/', AuthorListCreateView.as_view()),
    path('authors/<int:pk>/', AuthorDetailView.as_view()),
    path('categories/', CategoryListCreateView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),
    path('books/', BookListCreateView.as_view()),
    path('books/<int:pk>/', BookListCreateView.as_view()),
]
