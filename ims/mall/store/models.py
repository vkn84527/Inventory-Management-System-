from django.db import models

# Create your models here.
class Product(models.Model):
	regtime=models.DateTimeField(auto_now_add=True)
	pname=models.CharField(max_length=100)
	pdesc=models.CharField(max_length=200)
	pid= models.AutoField(primary_key=True)
	source=models.CharField(max_length=200)
	category=models.CharField(max_length=200)
	image=models.ImageField(upload_to="image", default=" ")
	stock=models.IntegerField(default=0)
	price=models.IntegerField()
	def __str__(self):
		return self.pname+"---"+str(self.pid)

class User(models.Model):
	regtime=models.DateTimeField(auto_now_add=True)
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=200,primary_key=True)
	passw=models.CharField(max_length=100)
	address=models.CharField(max_length=250)
	city=models.CharField(max_length=25)
	state=models.CharField(max_length=25)
	pincode=models.CharField(max_length=20)
	phone=models.CharField(max_length=15)
	dob=models.CharField(max_length=20)
	def __str__(self):
		return self.email