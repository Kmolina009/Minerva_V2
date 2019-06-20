from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Student(models.Model):
    name = models.CharField(max_length=50)
    grade = models.IntegerField(default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('students_detail', kwargs={'pk': self.id})


class Assignment(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    due_date = models.DateField()
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    assignments = models.ForeignKey(Assignment, on_delete=models.CASCADE)