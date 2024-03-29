from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=100)
    phonenumber=models.PositiveBigIntegerField()
    class Meta:
        db_table="Register"
class contactus(models.Model):
    firstname=models.TextField(max_length=100)
    lastname=models.TextField(max_length=100)
    email=models.EmailField(primary_key=True)
    comments=models.TextField(max_length=100)

    class Meta:
        db_table="contactus"

