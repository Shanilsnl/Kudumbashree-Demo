from django.db import models
class reg(models.Model):
	name=models.CharField(max_length=100,default='')
	email=models.CharField(max_length=100,default='')
	password=models.CharField(max_length=100,default='')
	usertype=models.CharField(max_length=100,default='')
class mem(models.Model):
	name=models.CharField(max_length=100,default='')
	email=models.CharField(max_length=100,default='')
	phone=models.CharField(max_length=100,default='')
	age=models.CharField(max_length=100,default='')
	aadhar=models.CharField(max_length=100,default='')
	status=models.CharField(max_length=100,default='Active')
	address=models.CharField(max_length=100,default='')
class att(models.Model):
	rg1=models.ForeignKey(mem,on_delete=models.CASCADE)
	date=models.CharField(max_length=100,default='')
	time=models.CharField(max_length=100,default='')
class loan(models.Model):
	rg1=models.ForeignKey(mem,on_delete=models.CASCADE)
	income=models.CharField(max_length=100,default='')
	loan_type=models.CharField(max_length=100,default='')
	amount=models.CharField(max_length=100,default='')
	status=models.CharField(max_length=100,default='')
	b_amount=models.CharField(max_length=100,default='')
class repay(models.Model):
	rg1=models.ForeignKey(loan,on_delete=models.CASCADE)
	date=models.CharField(max_length=100,default='')
	time=models.CharField(max_length=100,default='')
	r_amount=models.CharField(max_length=100,default='')

# Create your models here.
