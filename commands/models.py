from django.db import models

class CommandDB(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    favourite=models.BooleanField(default="False")

class Command(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    favourite=models.CharField(default="False",max_length=255)




 

    






