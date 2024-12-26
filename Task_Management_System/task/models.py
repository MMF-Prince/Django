from django.db import models
from category.models import Category
# Create your models here.

class Task(models.Model):
    taskTitle=models.CharField(max_length=150)
    taskDescription=models.TextField(max_length=500)
    is_completed=models.BooleanField(default=False)
    category=models.ManyToManyField(Category)

    def __str__(self):
        return self.taskTitle