from django.db import models

# Create your models here.

class StudentMOdel(models.Model):
    roll=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    adddress=models.TextField()

    def __str__(self):
        return f"name: {self.name}"