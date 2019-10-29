from django.db import models

class Author(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    publicationDate = models.DateField()
class List (models.Model) :
    items = models.CharField(max_length=300)
    finished = models.BooleanField(default= False)
    def __str__(self) :
        return self.items
    