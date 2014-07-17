from django.db import models

class User(models.Model):
   username = models.CharField(max_length=50)
   fname = models.CharField(max_length=50)
   lname = models.CharField(max_length=50)
   project = models.ForeignKey("Project")

class Project(models.Model):
    name = models.CharField(max_length=50)
    cpu_allocation = models.IntegerField(default=0)

