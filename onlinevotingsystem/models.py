from django.db import models

# Create your models here.
class Voter(models.Model):
    voter_name = models.CharField(max_length=100)
    voter_id =  models.IntegerField()