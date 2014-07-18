from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    project = models.ForeignKey("Project")
 
    def __unicode__(self):
        return "%s, %s (%s)" % (self.lname,self.fname,self.username)

class Project(models.Model):
    name = models.CharField(max_length=50)
    cpu_allocation = models.IntegerField(default=0)
  
    def __unicode__(self):
        return self.name

