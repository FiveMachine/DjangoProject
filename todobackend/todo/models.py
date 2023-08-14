from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    memo = models.TextField(blank=True)
    
    #set current time
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    
    # user who posted this
    
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
