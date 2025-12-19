from dataclasses import fields
from rest_framework import serializers
from .models import Author, Category, Book, Borrow
from django.contrib.auth.models import User


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    birth_date = serializers.DateField(allow_null=True, required=False)

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.birth_date = validated_data.get(
            'birth_date', instance.birth_date)
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), required=False)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), required=False)

    class Meta:
        model = Book
        fields = ["id", "title", "author", "category",]


class BorrowSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False)
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), required=False)

    class Meta:
        model = Borrow
        fields = "__all__"
