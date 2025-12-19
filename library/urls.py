from django.urls import path
from .views import AuthorListCreateView, AuthorDetailView
urlpatterns = [
    path('authors/', AuthorListCreateView.as_view()),
    path('authors/<int:pk>/', AuthorDetailView.as_view()),
]
