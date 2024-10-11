from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from musician.models import Musician


# Create your models here.
class Album(models.Model):
    album_name=models.CharField(max_length=100)
    release_date=models.DateField()
    rating=models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]

    )
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.album_name