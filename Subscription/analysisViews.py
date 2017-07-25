# -*- coding: utf-8 -*-
from django.http import HttpResponse
from .models import Subscription, Item, Analysis, AnalysisItem
from django.core import serializers
import json

def analysisItems(request, analysisId=''):
    analysisId = int(analysisId)
    analysis = Analysis.objects.get(id=analysisId)
    results = AnalysisItem.objects.filter(analysisID=analysis)
    items = [result.itemID for result in results if not result.itemID.isBuying]
    data = serializers.serialize('json', items)
    return HttpResponse(data, content_type='application/json')

def analysis(request, analysisId=''):
    analysisId = int(analysisId)
    analysis = Analysis.objects.get(id=analysisId)
    data = serializers.serialize('json', [analysis])
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return HttpResponse(data, content_type='application/json')
