from django.db import models

# Create your models here.

class Airline(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100, default='John Doe')


    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name