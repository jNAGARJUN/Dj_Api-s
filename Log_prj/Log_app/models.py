from django.db import models

# Create your models here.
class EmpDetails(models.Model):
    emp_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  

    def __str__(self):
        return self.username
