import django
from django.db import models

settings.configure()

#creates database fields for first_name and last_name

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

print(Person)