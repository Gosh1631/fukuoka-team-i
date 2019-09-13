from django.db import models

# Create your models here.
class Coin(models.Model):
    class Meta:
        db_table = 'money'
    sum_of_coin = models.IntegerField()
