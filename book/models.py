from django.db import models
from author.models import Author


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



