from django.db import models

# Create your models here.

class faculty(models.Model):
	name=models.CharField(max_length=100);
	email=models.CharField(max_length=100);
	pwd=models.CharField(max_length=100);
	qualification=models.CharField(max_length=100);
	phone=models.CharField(max_length=20);
	addr=models.CharField(max_length=1000);


