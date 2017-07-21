from bs4 import BeautifulSoup
import urllib2
import re

def urlBuilder(priceLow, priceHigh, keywords):
    return 'https://s.2.taobao.com/list/list.htm?q={0}&start={1}&end={2}&search_type=item&app=shopsearch'.format(keywords, int(priceLow), int(priceHigh))

def getItems(keywords, priceLow, priceHigh):
    crawlUrl = urlBuilder(priceLow, priceHigh, keywords)
    webStream = urllib2.urlopen(crawlUrl)
    soup = BeautifulSoup(webStream.read(), 'html.parser')
    total = int(soup.select_one('.item-num em').string)
    items = soup.select('.item-block')
    return (total, [parseItem(item) for item in items])
    
def parseItem(item):
    imgLink = item.select_one('.item-pic img')['src']
    price = item.select_one('.item-price em').string
    description = item.select_one('.item-brief-desc').string
    title = item.select_one('.item-pic a')['title']
    title = BeautifulSoup(title, 'html.parser').get_text()
    link = item.select_one('.item-pic a')['href']
    taobaoId = re.search(r'id=(\d+)', link).group(1)
    result = {}
    result['imgLink'] = imgLink
    result['price'] = float(price)
    result['title'] = title
    result['link'] = link
    result['description'] = description
    result['taobaoId'] = taobaoId
    return result
