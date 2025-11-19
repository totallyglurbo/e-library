from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    year = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    genre = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='media/')
    text = models.FileField(upload_to='media/')


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

