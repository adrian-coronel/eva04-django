from django.db import models

# Create your models here.
class User(models.Model):
  id_user =  models.AutoField(primary_key=True, auto_created=True)
  name = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50, unique=True)
  password = models.CharField(max_length=10)
  state = models.CharField(max_length=1, default='1')