from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email =  models.EmailField(blank=False)

    def __str__(self):
        return self.name


class Enquiry(models.Model):
    firstname = models.CharField(max_length=100, blank=False)
    lastname = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.firstname