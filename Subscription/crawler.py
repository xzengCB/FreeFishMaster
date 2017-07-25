from bs4 import BeautifulSoup
import urllib2
import re

def urlBuilder(priceLow, priceHigh, keywords):
    keywords = re.sub(r'\s+', '+', keywords)
    print keywords
    return 'https://s.2.taobao.com/list/list.htm?q={0}&start={1}&end={2}&search_type=item&app=shopsearch'.format(keywords, int(priceLow), int(priceHigh))

def getItems(keywords, priceLow, priceHigh):
    crawlUrl = urlBuilder(priceLow, priceHigh, keywords)
    webStream = urllib2.urlopen(crawlUrl)
    soup = BeautifulSoup(webStream.read(), 'html.parser')
    total = int(soup.select_one('.item-num em').string)
    items = soup.select('.item-block')
    nextPage = soup.select_one('.paginator-next')
    pageCrawled = 1
    if nextPage:
        crawPage('https:' + nextPage['href'], items, pageCrawled)
    return (total, [parseItem(item) for item in items])

def crawPage(crawlUrl, items, pageCrawled):
    webStream = urllib2.urlopen(crawlUrl)
    soup = BeautifulSoup(webStream.read(), 'html.parser')
    newItems = soup.select('.item-block')
    items += newItems
    nextPage = soup.select_one('.paginator-next')
    if nextPage and pageCrawled < 11:
        crawPage('https:' + nextPage['href'], items, pageCrawled + 1)
    
def parseItem(item):
    imgLink = item.select_one('.item-pic img')['data-ks-lazyload-custom']
    price = item.select_one('.item-price em').string
    description = item.select_one('.item-brief-desc').string
    title = item.select_one('.item-pic a')['title']
    title = BeautifulSoup(title, 'html.parser').get_text()
    link = item.select_one('.item-pic a')['href']
    taobaoId = re.search(r'id=(\d+)', link).group(1)
    result = {}
    result['imgLink'] = imgLink if imgLink else ''
    result['price'] = float(price)
    result['title'] = title if title else ''
    result['link'] = link if link else ''
    result['description'] = description if description else ''
    result['taobaoId'] = taobaoId
    return result
