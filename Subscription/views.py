# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Subscription, Item, Analysis, AnalysisItem
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .crawler import getItems
import threading
import msgSender

# Create your views here.

@csrf_exempt
def index(request, subID=''):
    if request.method == 'POST':
        return postSubscriptionResponse(request)
    if subID != '':
        return deleteSubscriptionResponse(int(subID))
    return getSubscriptionResponse(request)

def analysis(request, analysisId=''):
    analysisId = int(analysisId)
    print analysisId
    analysis = Analysis.objects.get(id=analysisId)
    results = AnalysisItem.objects.filter(analysisID=analysis)
    data = serializers.serialize('json', results)
    return HttpResponse(data, content_type='application/json')

def deleteSubscriptionResponse(subID):
    try:
        Subscription.objects.filter(id=subID).delete()
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=503)

def getSubscriptionResponse(request):
    subscription_list = Subscription.objects.order_by('-createdDT')[:5]
    data = serializers.serialize('json', subscription_list)
    return HttpResponse(data, content_type='application/json')

def postSubscriptionResponse(request):
    try:
        data = json.loads(request.body)
        subscription = Subscription.objects.create(
            keywords = data['keywords'],
            priceLow = float(data['priceLow']),
            priceHigh = float(data['priceHigh'])
        )
        subscription.save()
        thread = threading.Thread(target=crawlItems, args=(subscription.id, data['keywords'], data['priceLow'], data['priceHigh']))
        thread.start()
        return HttpResponse('success')
    except:
        return HttpResponse(status=503)

def crawlItems(subId, keywords, priceLow, priceHigh):
    totalNum, items = getItems(keywords, priceLow, priceHigh)
    analysis = createAnalysis(subId, totalNum)
    if len(items) > 0:
        msgSender.sendMsg(analysis.id)
    for item in items:
        saveCrawlItem(item, analysis.id)


def saveCrawlItem(item, analysisId):
    if not Item.objects.filter(taobaoId=int(item['taobaoId'])):
        resultItem = Item.objects.create(
            title = item['title'].encode('utf-8'),
            description = item['description'].encode('utf-8'),
            price = item['price'],
            link = item['link'].encode('utf-8'),
            imgLink = item['imgLink'].encode('utf-8'),
            taobaoId = int(item['taobaoId'])
        )
        resultItem.save()
        saveAnalysisItem(analysisId, resultItem.id)

def saveAnalysisItem(analysisId, itemId):
    analysisItem = AnalysisItem.objects.create(
        analysisID = Analysis.objects.get(id=analysisId),
        itemID = Item.objects.get(id=itemId)
    )
    analysisItem.save()
    return analysisItem

def createAnalysis(subId, totalNum):
    subscription = Subscription.objects.get(id=subId)
    analysis = Analysis.objects.create(subscriptionID=subscription, totalNum=totalNum)
    analysis.save()
    return analysis
    