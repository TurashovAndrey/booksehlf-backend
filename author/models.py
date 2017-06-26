from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=3000, null=True, blank=True)
    birth_date = models.DateField(null=True)
    death_date = models.DateField(null=True)