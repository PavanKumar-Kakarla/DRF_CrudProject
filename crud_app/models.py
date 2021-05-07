from django.db import models

# Create your models here.

class Bank(models.Model):
    Bank_Name = models.CharField(max_length=50)
    Bank_Location = models.CharField(max_length=50)
    def __str__(self):
        return self.Bank_Name

class Person(models.Model):
    Person_AccNo = models.CharField(max_length=30)
    Person_Name = models.CharField(max_length=50)
    Person_MobileNo = models.CharField(max_length=15)
    Person_Location = models.CharField(max_length=50)
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE)
    def __str__(self):
        return self.Person_Name
    
    