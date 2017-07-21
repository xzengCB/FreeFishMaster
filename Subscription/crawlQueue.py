from .models import Subscription, Item, Analysis, AnalysisItem
from .crawler import getItems
import msgSender

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
