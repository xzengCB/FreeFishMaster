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
from .crawlQueue import crawlItems

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
    subscription_list = Subscription.objects.order_by('-createdDT')
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
