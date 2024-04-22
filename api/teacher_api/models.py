from django.db import models

# Create your models here.
class Teacher(models.Model):
    Teacher_ID=models.IntegerField(max_length=3)
    Teacher_Name=models.CharField(max_length=50)
    Teacher_Department=models.TextField(choices=(('MBA','MBA'),('B.TECH','B.TECH'),('B.SC','B.SC'),('BCA','BCA')))
    Teacher_Degree=models.TextField(choices=(('MBA','MBA'),('B.TECH','B.TECH'),('B.SC','B.SC'),('BCA','BCA')))

