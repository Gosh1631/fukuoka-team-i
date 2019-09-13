from django.db import models

# Create your models here.
class Coin(models.Model):
    class Meta:
        db_table = 'money'
    sum_of_coin = models.IntegerField()
class Documents(model.Model):
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='media/', default='defo')
    uploaded_at = models.DateTimeField(auto_now_add=True)