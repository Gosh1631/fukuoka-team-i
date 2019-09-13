from django.shortcuts import render

# Create your views here.
class Coin(models.Model):
  class Meta:
    db_table = ''     
sum_of_coin = models.IntegerField()
