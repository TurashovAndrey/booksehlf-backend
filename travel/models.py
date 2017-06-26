from django.db import models
from book.models import Book

class Travel(models.Model):
    book = models.ForeignKey(
        Book,
        related_name='book',
        blank=False,
        null=False,
        help_text='Foreign key to book(book id)'
    )
    arrival = models.DateField(blank=False, null=False)
