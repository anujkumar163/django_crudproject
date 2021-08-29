from django.db import models

class Customer(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	address = models.CharField(max_length=100)
	pincode = models.IntegerField()
	mobile = models.CharField(max_length=20)