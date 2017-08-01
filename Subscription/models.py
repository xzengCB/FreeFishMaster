# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=200, blank=True)
    taobaoId = models.BigIntegerField(unique=True, db_index=True, blank=True)
    description = models.TextField(blank=True)
    price = models.FloatField(null=True)
    link = models.CharField(max_length=512, blank=True)
    imgLink = models.CharField(max_length=512, blank=True)
    isBuying = models.BooleanField(default=False)
    modifiedDT = models.DateTimeField(auto_now_add=True)
    createdDT = models.DateTimeField(auto_now_add=True)

class Subscription(models.Model):
    keywords = models.CharField(max_length=200)
    priceLow = models.FloatField(default=0)
    priceHigh = models.FloatField()
    recentAnalysisID = models.IntegerField(default=0)
    recentNotificationDT = models.DateTimeField(auto_now_add=True, null=True)
    createdDT = models.DateTimeField(auto_now_add=True)
    modifiedDT = models.DateTimeField(auto_now_add=True)

class Analysis(models.Model):
    subscriptionID = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    totalNum = models.IntegerField()
    createdDT = models.DateTimeField(auto_now_add=True)
    modifiedDT = models.DateTimeField(auto_now_add=True)

class AnalysisItem(models.Model):
    analysisID = models.ForeignKey(Analysis, on_delete=models.CASCADE)
    itemID = models.ForeignKey(Item)
    createdDT = models.DateTimeField(auto_now_add=True)
    modifiedDT = models.DateTimeField(auto_now_add=True)
