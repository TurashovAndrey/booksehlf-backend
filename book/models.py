from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=3000, null=True, blank=True)
    birth_date = models.DateField(null=True)
    death_date = models.DateField(null=True)


class Book(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=3000, null=True, blank=True)
    author = models.ForeignKey(
        Author,
        related_name='author',
        blank=False,
        null=False,
        help_text='Foreign key to author(author id)'
    )


class Travel(models.Model):
    book = models.ForeignKey(
        Book,
        related_name='book',
        blank=False,
        null=False,
        help_text='Foreign key to book(book id)'
    )
    arrival = models.DateField(blank=False, null=False)

