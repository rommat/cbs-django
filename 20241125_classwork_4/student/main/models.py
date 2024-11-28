from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    level = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Grade(models.Model):
    student = models.ForeignKey(Student, models.CASCADE, related_name="grades")
    subject = models.CharField(max_length=255)
    value = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.subject}: {self.value}'
