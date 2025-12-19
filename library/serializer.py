from dataclasses import fields
from rest_framework import serializers
from .models import Author, Category, Book


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


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = "__al__"


class BookSerializer(serializers.Serializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), required=False)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), required=False)

    class Meta:
        model = Book
        fields = "__all__"
