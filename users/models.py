from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)