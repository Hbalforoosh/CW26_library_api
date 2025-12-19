from django.db import router
from django.urls import path
from .views import AuthorListCreateView, AuthorDetailView, CategoryListCreateView, CategoryDetailView, BookListCreateView, BookDetailView
from .views import BorrowViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('borrows', BorrowViewSet, basename='borrow')
urlpatterns = []
urlpatterns += router.urls


# urlpatterns = [
#     path('authors/', AuthorListCreateView.as_view()),
#     path('authors/<int:pk>/', AuthorDetailView.as_view()),
#     path('categories/', CategoryListCreateView.as_view()),
#     path('categories/<int:pk>/', CategoryDetailView.as_view()),
#     path('books/', BookListCreateView.as_view()),
#     path('books/<int:pk>/', BookDetailView.as_view()),
# ]
