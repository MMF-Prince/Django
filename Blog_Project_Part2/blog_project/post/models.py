from django.db import models
from django.contrib.auth.models import User
from catagories.models import Catagory

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    catagory=models.ManyToManyField(Catagory) # one post can be in multiple catagory and vice versa
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title