from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):

        return f"{self.first_name} {self.last_name}"


class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):

        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField(blank=True, null=True)
    authors = models.ManyToManyField(Author, related_name="books")
    category = models.ForeignKey(
        Category, related_name="books", on_delete=models.CASCADE
    )
    published_date = models.DateField()
    available_copies = models.IntegerField(default=0)

    def __str__(self):

        return self.title


class Borrow(models.Model):
    user = models.ForeignKey(User, related_name="borrows", on_delete=models.CASCADE)

    book = models.ForeignKey(Book, related_name="borrows", on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):

        return f"{self.user.username} borrowed {self.book.title}"
