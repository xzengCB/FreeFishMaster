# coding: utf-8

import requests
import shortUrl

def sendMsg(analysisId):
    endpoint = 'https://api.twilio.com/2010-04-01/Accounts/AC2358ca95845def066530624681d09c29/Messages.json'
    resultUrl = shortUrl.getShortUrl(analysisId)

    payload = {
    'To': '+8618521592837',
    'From': '+13158474828',
    'Body': '【闲鱼Pro】已发现您订阅的闲鱼商品，点击{0}查看详情'.format(resultUrl)
    }

    res = requests.post(endpoint, data=payload)
    return res.text
