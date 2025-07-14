from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    inventory = models.PositiveIntegerField(default=0)
    daily_fee = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title
