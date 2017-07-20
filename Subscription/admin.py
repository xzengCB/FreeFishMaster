from django.contrib import admin

# Register your models here.

from .models import Subscription, Item, Analysis, AnalysisItem

admin.site.register(Subscription)
admin.site.register(Item)
admin.site.register(Analysis)
admin.site.register(AnalysisItem)
