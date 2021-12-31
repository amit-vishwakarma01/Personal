from django.db import models

# Create your models here.
class userlogin(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

class company_detail(models.Model):
	jobid = models.CharField(max_length=100,primary_key=True)
	username = models.CharField(max_length=100)
	compnay_name = models.CharField(max_length=100)
	ctc = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	date = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	mobile = models.CharField(max_length=100)
	status = models.CharField(max_length=100)
class profile(models.Model):
	username = models.CharField(max_length=100,primary_key=True)
	name = models.CharField(max_length=100) 
	mobile = models.CharField(max_length=100)
	dob = models.CharField(max_length=100)
class todolist(models.Model):
	todoid = models.CharField(max_length=100,primary_key=True)
	username = models.CharField(max_length=100)
	topic = models.CharField(max_length=100) 
	detail = models.CharField(max_length=1000)




