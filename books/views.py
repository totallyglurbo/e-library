from rest_framework import viewsets, filters, permissions
from django.contrib.auth.models import User
from .models import Book, Author
from .permissions import IsAdminUserOrReadOnly
from .serializers import UserSerializer, BookSerializer, AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author', 'genre']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer