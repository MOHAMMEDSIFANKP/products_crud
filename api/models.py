from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product')
    description = models.TextField(blank=True,null=True)
    price = models.PositiveIntegerField(blank=True, null= True)

    def __str__(self):
        return self.name if self.name else self.id


# Parent Model
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

# Child Model
class Student(Person):
    grade = models.CharField(max_length=10)
    school = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.grade}"
