# -*- coding: utf-8 -*-
import requests
import shortUrl
from .models import Analysis, Subscription

def sendMsg(analysisId):
    sub = Analysis.objects.get(id=analysisId).subscriptionID
    endpoint = 'https://api.twilio.com/2010-04-01/Accounts/AC159a981758701e70082c5af628168ec2/Messages.json'
    resultUrl = 'http://10.63.88.166:3000/matches/{0}'.format(analysisId)

    payload = {
    'To': '+8615800599746',
    'From': '+12672141443',
    'Body': '发自【闲鱼Pro】\n 物品: {1} \n 价格: {2} - {3} \n 点击 {0} 查看详情'.format(resultUrl, sub.keywords, sub.priceLow, sub.priceHigh)
    }

    res = requests.post(endpoint, data=payload)
    return res.text
