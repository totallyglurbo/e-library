from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Book, Author


class BookSerializer(serializers.HyperlinkedModelSerializer):

   class Meta:
       model = Book
       fields = ['title', 'author', 'year', 'genre', 'category', 'cover', 'text']

class AuthorSerializer(serializers.HyperlinkedModelSerializer):

   class Meta:
       model = Author
       fields = ['name', 'biography']


class UserSerializer(serializers.HyperlinkedModelSerializer):
   books = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', read_only=True)

   class Meta:
       model = User
       fields = ['url', 'id', 'username', 'books']