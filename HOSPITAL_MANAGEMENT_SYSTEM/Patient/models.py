from django.db import models

class UserModel(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    username = models.CharField(max_length=20,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=25)
    usertype = models.CharField(max_length=8)

    def __str__(self):
        return self.username

class PatientModel(models.Model):
    name = models.CharField(max_length=30)
    mobile =models.IntegerField()
    email = models.EmailField()
    gender =models.CharField(max_length=6)
    age =models.IntegerField()
    address =models.CharField(max_length=100)
    blood_group =models.CharField(max_length=4)
    username =models.ForeignKey(UserModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.name