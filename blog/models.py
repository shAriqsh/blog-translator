from django.db import models
from django.contrib.auth.models import User #User is class which comes fro another built-in database table 

STATUS= ((0,'Draft'),(1,'Publish'))
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=200)
    content= models.TextField()
    date_created=models.DateTimeField(auto_now_add=True) #this argument is used to save the current date when save key is pressed
    slug= models.SlugField(max_length=200,unique=True)
    author=models.ForeignKey(to=User, on_delete=models.CASCADE) #CASCADE deletes all the attributes of User when delete is pressed
    status= models.IntegerField(choices=STATUS,default=0)

    def __str__(self):
        return self.title
