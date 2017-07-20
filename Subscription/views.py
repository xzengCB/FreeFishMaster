from django.shortcuts import render
from django.http import HttpResponse
from .models import Subscription
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request, subID=''):
    if request.method == 'POST':
        return postSubscriptionResponse(request)
    if subID != '':
        return deleteSubscriptionResponse(int(subID))
    return getSubscriptionResponse(request)

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
        return HttpResponse('success')
    except:
        return HttpResponse(status=503)
