from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 150)
    email = models.EmailField(max_length = 200)

    def __str__(self):
        return self.name
