from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField(max_length=255)
    date = models.DateTimeField('date')
    tags = models.ManyToManyField(Tag)
    feedback = models.TextField(max_length=1023)  # TODO make it an object
    partitipatns = models.ManyToManyField(User)

    def __str__(self):
        return self.name
    
