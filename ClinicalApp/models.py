from django.db import models

# Create your models here.

class Patient(models.Model):
    lastname=models.CharField(max_length=20)
    firstname=models.CharField(max_length=20)
    age=models.IntegerField()

class ClinicalData(models.Model):
    COMPONENT_NAMES=[('hw','Height/Weight'),('bp','Blood Pressure'),('heartrate','Heart Rate')]
    componentname=models.CharField(choices=COMPONENT_NAMES,max_length=50)
    componentvalue=models.CharField(max_length=50)
    measuredatetime=models.DateField(auto_now_add=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)