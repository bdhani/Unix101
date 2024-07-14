from django.db import models

class Command(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=255, default="General")
    description = models.TextField()
    favourite = models.BooleanField(default=False)
    alias = models.CharField(max_length=255, blank=True, null=True, unique=True)




 

    






