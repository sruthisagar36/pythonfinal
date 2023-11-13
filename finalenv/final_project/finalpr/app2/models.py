from django.db import models


class Bank(models.Model):
       name=models.CharField(max_length=250)
       desc=models.TextField(max_length=250)
       def __str__(self):
         return self.name


