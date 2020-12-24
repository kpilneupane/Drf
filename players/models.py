from django.db import models


class Players(models.Model):
    name = models.CharField(max_length=50, null=False)
    age = models.IntegerField(null=True)
    country = models.CharField(max_length=50, null=False)
    current_club = models.CharField(max_length=50, null=True)



