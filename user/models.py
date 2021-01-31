from django.db import models
from datetime import datetime
# Create your models here.
class Foods(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=False)
    isready = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'foods'

class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    jumlah = models.IntegerField(null=False)
    foods = models.ForeignKey(Foods, on_delete=models.CASCADE , null=True)
    

    class Meta:
        db_table = 'users'

class Pesanans(models.Model):
    id = models.BigAutoField(primary_key=True)
    nama = models.CharField(max_length=200 , null=True)
    nomeja = models.IntegerField(null=False)
    keranjang = models.ForeignKey(Users, on_delete=models.CASCADE , null=True)
    
    
    class Meta:
        db_table = 'pesanans'