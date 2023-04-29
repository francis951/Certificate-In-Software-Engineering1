from django.db import models
gnder = (('Male', 'Male'), ('Female', 'Female'))
# Create your models here.
class GENQModels(models.Model):
    #bio
    f_name = models.CharField(max_length=250)
    l_name = models.CharField(max_length=250)
    date = models.DateField("Date of Birth")
    gender = models.CharField(max_length=100, null=True,choices=gnder)
    #locaton
    country = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    town = models.CharField(max_length=250)
    zip = models.IntegerField(default = 0)
    #address
    phone1 = models.IntegerField(default = 256)
    phone2 = models.IntegerField(default = 256)
    email = models.EmailField()