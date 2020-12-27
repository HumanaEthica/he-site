from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField(max_length=255)
    date = models.DateTimeField('date')

    def create(self): # __init__ 
        pass
    
    def edit(self):
        pass

    def add_participant(self):
        pass

    def __str__(self):
        return self.name
    

