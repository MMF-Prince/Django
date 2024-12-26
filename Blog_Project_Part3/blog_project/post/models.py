from django.db import models
from django.contrib.auth.models import User
from catagories.models import Catagory

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    catagory=models.ManyToManyField(Catagory) # one post can be in multiple catagory and vice versa
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='post/uploads/', blank=True,null=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=30)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"comments by {self.name}"