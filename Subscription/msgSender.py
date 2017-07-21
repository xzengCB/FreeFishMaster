# coding: utf-8

import requests
import shortUrl

def sendMsg(analysisId):
    endpoint = 'https://api.twilio.com/2010-04-01/Accounts/AC616c2a9691d0f5c3b5123d3a44a70302/Messages.json'
    resultUrl = 'http://mchen.cbapac.net:3000/matches/{0}'.format(analysisId)

    payload = {
    'To': '+8615800599746',
    'From': '+12566678498',
    'Body': '【闲鱼Pro】已发现您订阅的闲鱼商品，点击{0}查看详情'.format(resultUrl)
    }

    res = requests.post(endpoint, data=payload)
    return res.text
