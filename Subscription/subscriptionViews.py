# -*- coding: utf-8 -*-
from django.http import HttpResponse
from .models import Subscription 
from django.core import serializers
import json

def subscription(request, subscriptionId=''):
    subscriptionId = int(subscriptionId)
    subscription = Subscription.objects.get(id=subscriptionId)
    data = serializers.serialize('json', [subscription])
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return HttpResponse(data, content_type='application/json')
