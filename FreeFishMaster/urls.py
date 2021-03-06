"""FreeFishMaster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Subscription import analysisViews, subscriptionViews

urlpatterns = [
    url(r'^api/subscriptions', include('Subscription.urls')),
    url(r'^api/subscription/(?P<subscriptionId>[0-9]{1,11})$', subscriptionViews.subscription, name='subscription'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/analysisItems/(?P<analysisId>[0-9]{1,11})$', analysisViews.analysisItems, name='analysisItems'),
    url(r'^api/analysis/(?P<analysisId>[0-9]{1,11})$', analysisViews.analysis, name='analysis'),
]
