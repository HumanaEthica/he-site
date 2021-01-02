from django.db import models
from  django.contrib.auth.models import AbstractUser

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Localization(models.Model):
    class Meta:
        unique_together = (('address', 'city', 'postal_code', 'country'),)

    address = models.TextField(max_length=255) # ?
    city = models.CharField(max_length=127)
    postal_code = models.CharField(max_length=31)
    country = models.CharField(max_length=63)

    def __str__(self):
        return self.address + self.city

class User(AbstractUser):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1023)
    localization = models.ForeignKey(Localization, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


# if ONG, Private organiztion, etc.
# to be populated before running the app
class OrganizationTypes(models.Model):
    type = models.CharField(max_length=255)

class Organization(models.Model):
    name = models.CharField(max_length=127)
    organization_type = models.ForeignKey(OrganizationTypes)
    staff = models.ManyToManyField(User)


class Feedback(models.Model):
    text = models.TextField(max_length=1023)
    author = models.ForeignKey(User)#???)
    is_positive = models.BooleanField()  # TODO maybe change 5 star rating
    date = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField(max_length=255)
    date = models.DateTimeField('date')
    tags = models.ManyToManyField(Tag)
    feedback = models.OneToManyField(Feedback)
    participants = models.ManyToManyField(User)
    organizer = models.ForeignKey(Organization)

    def __str__(self):
        return self.name