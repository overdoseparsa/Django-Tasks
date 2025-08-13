from rest_framework import serializers
from .models import Author , Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name' , 'birth_year')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title' , 'publication_year' ,'author')

        