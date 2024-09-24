from django.db import models
from author.models import Author
from catagories.models import Catagory

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    catagory=models.ManyToManyField(Catagory) # one post can be in multiple catagory and vice versa
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title