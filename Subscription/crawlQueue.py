# -*- coding: utf-8 -*-
from .models import Subscription, Item, Analysis, AnalysisItem
from .crawler import getItems
import msgSender

def crawlItems(subId, keywords, priceLow, priceHigh):
    totalNum, items = getItems(keywords.encode('gbk'), priceLow, priceHigh)
    analysis = createAnalysis(subId, totalNum)
    flag = False
    for item in items:
        if saveCrawlItem(item, analysis.id) and not judgeIsBuying(item['title'], item['description']):
            flag = True
    if flag:
        sub = Subscription.objects.get(id=subId)
        sub.recentAnalysisID = analysis.id
        sub.save()
        msgSender.sendMsg(analysis.id)

def saveCrawlItem(item, analysisId):
    flag = False
    if not Item.objects.filter(taobaoId=int(item['taobaoId'])):
        flag = True
        resultItem = Item.objects.create(
            title = item['title'],
            description = item['description'],
            price = item['price'],
            link = item['link'],
            imgLink = item['imgLink'],
            taobaoId = int(item['taobaoId'])
        )
        resultItem.isBuying = judgeIsBuying(resultItem.title, resultItem.description)
        resultItem.save()
        saveAnalysisItem(analysisId, resultItem.id)
    return flag

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

def judgeIsBuying(title, desc):
    isBuyingTitle = (u"求购" in title or u"收" in title)
    isBuyingDesc = (u"求购" in desc or u"收" in desc)
    return isBuyingTitle or isBuyingDesc
