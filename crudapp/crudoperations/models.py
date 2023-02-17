from django.db import models

# Create your models here.
class Students(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=250, blank = False, name = "name") 
    email = models.EmailField(max_length=250, blank=False, name = "email")
    marks = models.CharField(max_length=250, blank=False, name = "marks")

