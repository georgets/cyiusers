from django.db import models
import lists 

class User(models.Model):
    username = models.CharField(max_length=50,verbose_name="username")
    fname = models.CharField(max_length=50,verbose_name="First Name")
    lname = models.CharField(max_length=50,verbose_name="Last Name")
    project = models.ForeignKey("Project",verbose_name="Project")

    def __unicode__(self):
        return "%s, %s (%s)" % (self.lname,self.fname,self.username)

class Project(models.Model):
    name = models.CharField(max_length=50,verbose_name="Project ID",null=False)
    title = models.CharField(max_length=50,verbose_name="Project Title",null=True) 
    cpu_allocation = models.IntegerField(default=0,verbose_name="CPU Allocation")
    linklings_id = models.CharField(max_length=50,verbose_name="Linklings ID",null=True)
    pi_email = models.EmailField(verbose_name="PI Email",null=True)
    pi =  models.ForeignKey("User",verbose_name="PI",related_name="project_pi",null=True)
    scientific_field = models.CharField(max_length=50,verbose_name="Project ID",null=True,choices=SCIENTIFIC_FIELDS)

    def __unicode__(self):
        return self.name

#	Scientific Field 
#	PI
#	Institution/Company
#	Country
#	Access Type
#	Decision
#	Project(LinkSEEM or Cy-Tera)
#	HPC System (CyI or BA)
#	Start Date
#	End Date
#	Call Number
#	CPU hours requested
#	GPU hours requested
#	Storage required (GB)
#	CPU hours allocated
#	GPU hours allocated
#	Storage allocated (GB)
#	Percent of request for CPU
#	Percent of request for GPU
#	Percent of request for storage
#	CPU hours used
#	GPU hours used
#	CPU Penalty
#	GPU Penalty
#	Overall Technical Review 
#	Overall Scientific Review (average)
#	Comments from reviewers
#	Scientific Reviewer 1 Name
#	Scientific Reviewer 1 Email
#	Scientific Reviewer 2 Name
#	Scientific Reviewer 2 Email
#	Scientific Reviewer 3 Name
#	Scientific Reviewer 3 Email
#	Scientific Reviewer 4 Name
#	Scientific Reviewer 4 Email
#	Summary of the project
#	Total number of active users
#	Name of User 1
#	Email of User 1
#	Institution/Company of User 1
#	Username of user 1
#	Name of User 2
#	Email of User 2
#	Institution/Company of User 2
#	Username of user 3
#	Name of User 3
#	Email of User 3
#	Institution/Company of User 3
#	Username of user 4
#	Name of User 4
#	Email of User 4
#	Institution/Company of User 4
#	Username of user 4
#	Name of User 5
#	Email of User 5
#	Institution/Company of User 5
#	Username of user 5
#	Name of User 6
#	Email of User 6
#	Institution/Company of User 6
#	Username of user 6
#	Name of User 7
#	Email of User 7
#	Institution/Company of User 7
#	Username of user 7
#	Name of User 8
#	Email of User 8
#	Institution/Company of User 8
#	Username of user 8
#	Name of User 9
#	Email of User 9
#	Institution/Company of User 9
#	Username of user 9
#	Name of User 10
#	Email of User 10
#	Institution/Company of User 10
#	Username of user 10
#	Number of Publications/reports
#	Number of Presentations/Talks
#	Number of Theses
 

