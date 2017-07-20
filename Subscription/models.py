from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    link = models.CharField(max_length=512)
    imgLink = models.CharField(max_length=512)
    modifiedDT = models.DateTimeField(auto_now_add=True)
    createdDT = models.DateTimeField(auto_now_add=True)

class Subscription(models.Model):
    keywords = models.CharField(max_length=200)
    priceLow = models.FloatField(default=0)
    priceHigh = models.FloatField()
    createdDT = models.DateTimeField(auto_now_add=True)
    modifiedDT = models.DateTimeField(auto_now_add=True)

class Analysis(models.Model):
    subscriptionID = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    createdDT = models.DateTimeField(auto_now_add=True)
    modifiedDT = models.DateTimeField(auto_now_add=True)

class AnalysisItem(models.Model):
    analysisID = models.ForeignKey(Analysis, on_delete=models.CASCADE)
    itemID = models.ForeignKey(Item)
    createdDT = models.DateTimeField(auto_now_add=True)
    modifiedDT = models.DateTimeField(auto_now_add=True)

