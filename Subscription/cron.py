import datetime
from .models import Subscription
from .crawlQueue import crawlItems
def handleSubscriptions():
    subs = Subscription.objects.all()
    for sub in subs:
        crawlItems(sub.id, sub.keywords, sub.priceLow, sub.priceHigh)
