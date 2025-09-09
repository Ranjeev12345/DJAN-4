from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)  # match MySQL column
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    year_published = models.IntegerField()

    class Meta:
        db_table = "books_book"   # matches your MySQL table

    def __str__(self):
        return self.name
