from django.db import models

class Users(models.Model):
    payment_method_token = models.CharField(max_length=200)

class Articles(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    amount = models.FloatField()

class Orders(models.Model):
    user = models.ForeignKey(Users)
    article = models.ForeignKey(Articles)
